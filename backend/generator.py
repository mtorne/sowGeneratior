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
    TextContent
)
import uuid
from docxtpl import DocxTemplate



# OCI config
config = oci.config.from_file("~/.oci/config", "DEFAULT")
client = oci.generative_ai_inference.GenerativeAiInferenceClient(config)

# OCID del compartment i model (posa aquí els teus valors reals)
compartment_id = "ocid1.compartment.oc1..aaaaaaaaw5klhwyzaxvto4vzwnavevivn75nfuv4fdanlbjux4fuk6tv5geq"
#model_id = "ocid1.generativeaimodel.oc1.eu-frankfurt-1.amaaaaaask7dceya4tdabclcsqbc3yj2mozvvqoq5ccmliv3354hfu3mx6bq"
model_id = "ocid1.generativeaimodel.oc1.eu-frankfurt-1.amaaaaaask7dceyaaypm2hg4db3evqkmjfdli5mggcxrhp2i4qmhvggyb4ja"

class PromptRequest(BaseModel):
    prompt: str

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
                max_tokens=300,
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


def generar_documento(datos):
    prompt = f"""
Genera un resumen ejecutivo y una descripción técnica del proyecto "{datos['proyecto']}" para el cliente {datos['cliente']} utilizando los siguientes servicios de Oracle Cloud: {', '.join(datos['servicios_oci'])}.
"""

    resultado = generate_chat(prompt)
    texto_generado = resultado["response"]  # ✅ Accede al texto

    resumen = texto_generado.split("##")[0].strip()
    detalles = "\n".join(texto_generado.split("##")[1:]).strip()

    env = Environment(loader=FileSystemLoader("."))
    plantilla = env.get_template("plantilla.sow.md.j2")
     # Carga plantilla Word
    doc = DocxTemplate("Application_Validation_Template.docx")



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

    doc.render(contenido)

    nombre_base = f"salida_{uuid.uuid4().hex}"
    nombre_archivo = f"{nombre_base}.docx"
    doc.save(nombre_archivo)
    ##with open(f"{nombre_base}.md", "w") as f:
    ##    f.write(contenido)

    ##subprocess.run(["pandoc", f"{nombre_base}.md", "-o", f"{nombre_base}.docx"])
    ##return f"{nombre_base}.docx"
    return nombre_archivo

