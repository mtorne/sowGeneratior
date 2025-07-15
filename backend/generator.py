import oci
from fastapi import FastAPI, HTTPException
import os
import requests
from jinja2 import Environment, FileSystemLoader
import subprocess
from pydantic import BaseModel
from oci.generative_ai_inference.models import (
    GenerateTextDetails,
    OnDemandServingMode,
    CohereLlmInferenceRequest,
    ChatDetails,
    GenericChatRequest,
    CohereChatRequest,
    SystemMessage,
    TextContent,
    Message,
    ChatContent
)
import uuid
from docxtpl import DocxTemplate
from pathlib import Path
from openai import OpenAI
from xai_sdk import Client
from xai_sdk.chat import user, system
from dotenv import load_dotenv

load_dotenv()



# OCI config
config = oci.config.from_file("~/.oci/config", "DEFAULT")
client = oci.generative_ai_inference.GenerativeAiInferenceClient(config)

# OCID del compartment i model (posa aquí els teus valors reals)
compartment_id = "ocid1.compartment.oc1..aaaaaaaaw5klhwyzaxvto4vzwnavevivn75nfuv4fdanlbjux4fuk6tv5geq"
#model_id = "ocid1.generativeaimodel.oc1.eu-frankfurt-1.amaaaaaask7dceya4tdabclcsqbc3yj2mozvvqoq5ccmliv3354hfu3mx6bq"
model_id = "ocid1.generativeaimodel.oc1.eu-frankfurt-1.amaaaaaask7dceyaaypm2hg4db3evqkmjfdli5mggcxrhp2i4qmhvggyb4ja"
model_id_llama = "ocid1.generativeaimodel.oc1.eu-frankfurt-1.amaaaaaask7dceya4tdabclcsqbc3yj2mozvvqoq5ccmliv3354hfu3mx6bq"

client_openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
grok_client = Client(api_key=os.getenv("XAI_API_KEY"))



class PromptRequest(BaseModel):
    prompt: str


def generar_prompt(datos: dict, file_path: str = "prompt1.txt") -> str:
    """
    Genera un prompt evaluando expresiones tipo f-string desde un archivo.

    :param datos: Diccionario con las variables necesarias
    :param file_path: Ruta al archivo del prompt
    :return: Prompt generado
    """
    path = Path(file_path)
    with open(path, encoding="utf-8") as f:
        prompt_template = f.read()

    # Evalúa la plantilla como una f-string con acceso a datos
    try:
        prompt = eval(f"f'''{prompt_template}'''", {"datos": datos})
        return prompt
    except Exception as e:
        raise ValueError(f"Error al generar el prompt: {e}")


def generate_chat(prompt: str) -> str:
    try:
        chat_details = ChatDetails(
            compartment_id=compartment_id,
            serving_mode=OnDemandServingMode(
                serving_type="ON_DEMAND",
                model_id=model_id
            ),
            chat_request=CohereChatRequest(
                api_format="COHERE",
                max_tokens=3000,
                temperature=0.7,
                top_k=0,
                top_p=1.0,
                message=prompt,
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


def generate_chat_llama(prompt: str) -> dict:
    try:
        # Prepare the inner content
        content = TextContent()
        content.text = prompt

        # Create a user message with the content
        message = Message()
        message.role = "USER"
        message.content = [content]

        # Construct the chat request
        chat_request = GenericChatRequest()
        chat_request.api_format = GenericChatRequest.API_FORMAT_GENERIC
        chat_request.messages = [message]
        chat_request.max_tokens = 4000
        chat_request.temperature = 0.7
        chat_request.top_p = 1.0
        chat_request.top_k = -1.0
        chat_request.frequency_penalty = 0.0
        chat_request.presence_penalty = 0.0

        # Build chat details
        chat_detail = ChatDetails()
        chat_detail.compartment_id = compartment_id
        chat_detail.serving_mode = OnDemandServingMode(
            model_id=model_id_llama  # Ensure this is for a GENERIC-compatible model (e.g., LLaMA)
        )
        chat_detail.chat_request = chat_request

        # Send chat request
        opc_retry_token = str(uuid.uuid4())
        opc_request_id = str(uuid.uuid4())

        response = client.chat(
            chat_details=chat_detail,
            opc_retry_token=opc_retry_token,
            opc_request_id=opc_request_id
        )

    
        generated_text = response.data.chat_response.choices[0].message.content[0].text

        return {"response": generated_text}

    except Exception as e:
        print(f"❌ Error during LLaMA chat generation: {e}")
        return {"error": str(e)}



def generate_chat_gpt4(prompt: str) -> dict:
    
    try:
        response = client_openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Ets un assistent que genera documents tècnics."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=4096
        )

        return {"response": response.choices[0].message.content}

    except Exception as e:
        print("❌ Error during GPT-4 chat generation:")
        print(e)
        return "Error generant document."


def generate_chat_grok4(prompt: str) -> dict:
    try:
        
        chat = grok_client.chat.create(model="grok-4")
        chat.append(system("You are Cloud Architect specilized in OCI, helpful AI assistant."))
        chat.append(user(prompt))

        response = chat.sample()

        return {"response": response.content}

    except Exception as e:
        print("❌ Error during Grok-4 chat generation:")
        print(e)
        return {"error": "Error generant document."}




def generar_documento(datos):


    prompt2 = generar_prompt(datos,"prompt2.txt")
    prompt3 = generar_prompt(datos,"prompt3.txt")
    
    prompt_used = prompt2

    #resultado = generate_chat_llama(prompt_used)
    #resultado = generate_chat(prompt_used)
    #resultado = generate_chat_gpt4(prompt_used)
    resultado = generate_chat_grok4(prompt_used)
    texto_generado = resultado["response"]  # ✅ Accede al texto

    resumen = texto_generado.split("##")[0].strip()
    detalles = "\n".join(texto_generado.split("##")[1:]).strip()

    env = Environment(loader=FileSystemLoader("."))
    plantilla = env.get_template("plantilla.sow.md.j2")


    contenido = {
    "cliente": datos.get('cliente'),
    "proyecto": datos.get('proyecto'),
    "servicios_oci": datos.get('servicios_oci', []),
    "resumen": resumen,
    "detalles": detalles,

    # Optional extras
    "isv_name": datos.get('isv_name'),
    "app_name": datos.get('app_name'),
    "fecha": datos.get('fecha'),
    "version": datos.get('version'),

    "historial": datos.get('historial', []),
    "estado": datos.get('estado'),
    "participantes": datos.get('participantes', []),
    "perfil_empresa": datos.get('perfil_empresa', {}),
    "app_descripcion": datos.get('app_descripcion'),
    "app_tecnologias": datos.get('app_tecnologias'),
    "app_entorno": datos.get('app_entorno'),
    "alcance": datos.get('alcance'),
    "hitos": datos.get('hitos', []),
    "criterios": datos.get('criterios', []),
    "arquitectura_actual": datos.get('arquitectura_actual', {}),
    "arquitectura_objetivo_diagrama": datos.get('arquitectura_objetivo_diagrama'),
    "arquitectura_objetivo_componentes": datos.get('arquitectura_objetivo_componentes', []),
    "detalles_implementacion": datos.get('detalles_implementacion'),
    "feedback_isv": datos.get('feedback_isv'),
    "feedback_oracle": datos.get('feedback_oracle')
    }

    
    # Render the template with the context
    rendered_content = plantilla.render(contenido)

    nombre_base = f"salida_{uuid.uuid4().hex}"
    nombre_archivo = f"{nombre_base}.docx"

    # Write the rendered content to a markdown file
    with open(f"{nombre_base}.md", "w", encoding="utf-8") as f:
       f.write(rendered_content)  # Write the rendered template, not the dictionary

    # Convert to docx using pandoc
    #subprocess.run(["pandoc", f"{nombre_base}.md", "-o", nombre_archivo])
    return rendered_content

