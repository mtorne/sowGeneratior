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

   # In generator.py, update the contenido dictionary to match template variable names:
    contenido = {
     "isv_name": datos.get('isv_name'),
     "app_name": datos.get('app_name'),
     "version": datos.get('version'),
     "date": datos.get('fecha'),
    
     # Project Participants
     "participants": datos.get('participantes', []),
    
     # ISV Company Profile
     "company_profile": {
        "legal_name": datos.get('perfil_empresa', {}).get('nombre_legal'),
        "country": datos.get('perfil_empresa', {}).get('pais'),
        "description": datos.get('perfil_empresa', {}).get('descripcion'),
        "industry": datos.get('perfil_empresa', {}).get('industria'),
        "website": datos.get('perfil_empresa', {}).get('sitio_web')
     },
    
     # Project Overview
     "project_overview": datos.get('resumen'),
    
     # Scope
     "scope": datos.get('alcance'),
    
     # Major Project Milestones
     "milestones": datos.get('hitos', []),
    
     # Acceptance Criteria
     "acceptance_criteria": datos.get('criterios', []),
    
     # Current State Architecture
     "current_architecture": {
        "diagram_url": datos.get('arquitectura_actual', {}).get('diagrama'),
        "description": datos.get('arquitectura_actual', {}).get('descripcion')
     },
    
     # Technology Stack
     "technology_stack": datos.get('app_tecnologias', []),
    
     # OCI Service Sizing
     "oci_services": datos.get('servicios_oci', []),
    
     # Future State Architecture
     "future_architecture": {
        "diagram_url": datos.get('arquitectura_objetivo_diagrama'),
        "overview": datos.get('detalles'),
        "components": datos.get('arquitectura_objetivo_componentes', [])
     },
    
     # Implementation Details
     "implementation_details": datos.get('detalles_implementacion'),
    
     # Closing Feedback
     "closing_feedback": {
        "isv": datos.get('feedback_isv'),
        "oracle": datos.get('feedback_oracle')
     },
    
     # Copyright
     "copyright_year": "2023"  # or get from datos if available
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

