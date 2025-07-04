from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import oci
from oci.generative_ai_inference.models import (
    GenerateTextDetails,
    OnDemandServingMode,
    CohereLlmInferenceRequest,
    ChatDetails,
    GenericChatRequest,
    CohereChatRequest,
    SystemMessage,
    TextContent
)
import uuid

app = FastAPI()

# Configura CORS per permetre frontend local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# OCI config
config = oci.config.from_file("~/.oci/config", "DEFAULT")
client = oci.generative_ai_inference.GenerativeAiInferenceClient(config)

# OCID del compartment i model (posa aquí els teus valors reals)
compartment_id = "ocid1.compartment.oc1..aaaaaaaaw5klhwyzaxvto4vzwnavevivn75nfuv4fdanlbjux4fuk6tv5geq"
#model_id = "ocid1.generativeaimodel.oc1.eu-frankfurt-1.amaaaaaask7dceya4tdabclcsqbc3yj2mozvvqoq5ccmliv3354hfu3mx6bq"
model_id = "ocid1.generativeaimodel.oc1.eu-frankfurt-1.amaaaaaask7dceyaaypm2hg4db3evqkmjfdli5mggcxrhp2i4qmhvggyb4ja"

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
def generate_text(request: PromptRequest):
    try:
        details = GenerateTextDetails(
            compartment_id=compartment_id,
            serving_mode=OnDemandServingMode(
                serving_type="ON_DEMAND",
                model_id=model_id
            ),
            inference_request=CohereLlmInferenceRequest(
                runtime_type="COHERE",
                prompt=request.prompt,
                is_stream=False,
                num_generations=1,
                is_echo=False,
                max_tokens=300,
                temperature=0.7,
                top_k=0,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
                stop_sequences=[],
                return_likelihoods="NONE",
                truncate="NONE"
            )
        )

        # Opcional: genera un token únic per la petició
        opc_retry_token = str(uuid.uuid4())
        opc_request_id = str(uuid.uuid4())

        response = client.generate_text(
            generate_text_details=details,
            opc_retry_token=opc_retry_token,
            opc_request_id=opc_request_id
        )

        return {"response": response.data.generated_text}

    except Exception as e:
        # Mostra l’error a consola i retorna 500
        print(f"Error a generate_text: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generatechat")
def generate_chat(request: PromptRequest):
    try:
        chat_details = ChatDetails(
            compartment_id=compartment_id,
            serving_mode=OnDemandServingMode(
                serving_type="ON_DEMAND",
                model_id=model_id
            ),
            chat_request=CohereChatRequest(
                api_format="COHERE",
                max_tokens=300,
                temperature=0.7,
                top_k=0,
                top_p=1.0,
                message=request.prompt,
                frequency_penalty=0.0,
                presence_penalty=0.0,
            )
        )

        opc_retry_token = str(uuid.uuid4())
        opc_request_id = str(uuid.uuid4())

        response = client.chat(
            chat_details=chat_details,
            opc_retry_token=opc_retry_token,
            opc_request_id=opc_request_id
        )

        print("Resposta completa de chat_response:", response.data)  

        # El text generat normalment està a response.data.choices[0].message.content.text
        chat_response_text =response.data.chat_response.text 
        # El format pot variar segons la versió, mirarem per generar text:

        return {"response": chat_response_text}

    except oci.exceptions.ServiceError as e:
        raise HTTPException(status_code=e.status, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

