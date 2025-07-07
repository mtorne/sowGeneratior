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



# OCI config
config = oci.config.from_file("~/.oci/config", "DEFAULT")
client = oci.generative_ai_inference.GenerativeAiInferenceClient(config)

# OCID del compartment i model (posa aquí els teus valors reals)
compartment_id = "ocid1.compartment.oc1..aaaaaaaaw5klhwyzaxvto4vzwnavevivn75nfuv4fdanlbjux4fuk6tv5geq"
#model_id = "ocid1.generativeaimodel.oc1.eu-frankfurt-1.amaaaaaask7dceya4tdabclcsqbc3yj2mozvvqoq5ccmliv3354hfu3mx6bq"
model_id = "ocid1.generativeaimodel.oc1.eu-frankfurt-1.amaaaaaask7dceyaaypm2hg4db3evqkmjfdli5mggcxrhp2i4qmhvggyb4ja"
model_id_llama = "ocid1.generativeaimodel.oc1.eu-frankfurt-1.amaaaaaask7dceya4tdabclcsqbc3yj2mozvvqoq5ccmliv3354hfu3mx6bq"

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

        # Extract response
        #chat_result = response.data.chat_response.text
        #assistant_message = response.data.chat_response.message
        #assistant_content = assistant_message.content[0].text
        #texto = extract_generated_text(response)
        # Inspecciona toda la respuesta para entender su estructura
        ##print(response.data)
        ##print(response.data.chat_response)
        ##print(dir(response.data.chat_response))
    
        generated_text = response.data.chat_response.choices[0].message.content[0].text

        return {"response": generated_text}

    except Exception as e:
        print(f"❌ Error during LLaMA chat generation: {e}")
        return {"error": str(e)}


def extract_generated_text(response):
    # Navigate to choices -> first item -> message -> content -> first item -> text
    try:
          # Convert Response object to dict
        choices = response["chat_response"]["choices"]
        #if not choices:
        #    return None

        message = choices[0]["message"]
        content = message["content"]
        ##if not content:
         ##   return None

        text = content[0]["text"]
        return text

    except Exception as e:
        print(f"Error extracting generated text: {e}")
        return None


def generar_documento(datos):

    prompt2 = f"""Generate a **Statement of Work (SoW)** document for an **Oracle Cloud Infrastructure (OCI) Application Validation** project for client **{datos['cliente']}**, using the following OCI services: **{', '.join(datos['servicios_oci'])}**.

Follow the **exact section structure and technical detail style** as shown in the reference document `Comarch-Telco-OSS-ISV-v0.2`.

---

### 1. Document Header
- ISV: **[datos['cliente']]**
- Application: **[datos['proyecto']]**
- Type: **Statement of Work**
- Date: **[fecha_actual]**
- Version: **0.1**
- Include Oracle's standard **Confidentiality Disclaimer** (as in the original document).

---

### 2. SoW Version History Table
- 3 to 5 entries simulating evolving versions
- Table with: **Version #, Date, Revised By, Description of Change**

---

### 3. Status and NEXT STEPS
- Current project status: *Planning / In Progress / Completed*
- Next 3 actions required with **Owner, Description**

---

### 4. Project Participants Table
- Two tables: one for **Oracle**, one for **Client ({datos['cliente']})**
- Include: **Name, Role, Email**
- Keep color-coding format: Tan for Oracle, Green for Client

---

### 5. Project Framework
- Summarize collaboration mode between Oracle and {datos['cliente']}, including:
  - Responsibility areas
  - Feedback loops
  - Expected validation duration (2-3 weeks)

---

### 6. Required Contribution From Client
- Clearly list what {datos['cliente']} must provide:
  - Technical resources
  - Diagrams or architectural artifacts
  - Access to dev/test environment

---

### 7. Expected Deliverables From Oracle ISV Labs
- Standard Oracle outputs:
  - Terraform modules
  - Target architecture in OCI
  - Technical documentation
  - CI/CD integration examples if relevant

---

### 8. Cloud Environment Used
- Specify if PoC will run in:
  - PoC Tenancy
  - Temporary Test Tenancy
  - Client tenancy (if already onboarded)

---

### 9. {datos['cliente']} Company Profile
- Legal Name
- Country of Operations
- 2-3 line Company Overview
- Website link

---

### 10. In-Scope Application: {datos['proyecto']}
- Application Name
- General Description
- Key Technologies
- Current Hosting: On-prem / Public Cloud / Hybrid

---

### 11. Project Overview
- **Validation Summary**: {datos['descripcion_validacion']}
- Use bullet points for:
  - Desired outcome
  - Scope boundaries
  - Joint goals

---

### 12. Scope
- **In-Scope Items**: (e.g., PostgreSQL setup, streaming config, OKE deployment)
- **Out-of-Scope Items**: (e.g., Production migration, Licensing setup, SLA support)
- Validation boundaries and limitations

---

### 13. Major Project Milestones
| Milestone                         | Target Date | Completed | Comments                 |
|----------------------------------|-------------|-----------|--------------------------|
| Kickoff with Cloud Architect     | YYYY-MM-DD  |           |                          |
| OCI Network Setup                | YYYY-MM-DD  |           |                          |
| Terraform Code Finalization      | YYYY-MM-DD  |           |                          |
| Application Deployment in OCI    | YYYY-MM-DD  |           |                          |
| Final Validation & Review        | YYYY-MM-DD  |           |                          |

---

### 14. Acceptance Criteria
- Table format:
| Capability/Metric                                | Acceptance Criteria                                                       | Status  |
|--------------------------------------------------|----------------------------------------------------------------------------|---------|
| Kubernetes Deployment                            | {datos['proyecto']} runs successfully on OCI OKE                 | TBD     |
| OCI Streaming                                     | Kafka integration tested using OSS workloads                              | TBD     |
| PostgreSQL                                        | DB deployed, configured, accessible                                       | TBD     |
| Monitoring                                        | Basic metrics visible in OCI Monitoring dashboard                         | TBD     |
| Security                                          | IAM + NSG + Encryption in Transit & At Rest                               | TBD     |

---

### 15. Current State Architecture
- **Diagram Description**: Describe current setup (K8s clusters, Kafka, DB, etc.)
- **Tech Stack**: Docker, Helm, PostgreSQL, Java, etc.
- **Known Issues/Pain Points**: e.g., manual deployments, scaling issues

---

### 16. Target OCI Architecture
- Describe how the following OCI services will be used: {', '.join(datos['servicios_oci'])}
- Include:
  - **Service Mapping** table (what maps to what)
  - **Component Interaction**
  - **Diagram Placeholder** (describe layout in text)

---

### 17. Implementation Details and Configuration Settings
- For each service in {', '.join(datos['servicios_oci'])}, include:
  - Provisioning shape/config
  - IAM Policies or NSGs applied
  - Helm/Terraform usage if relevant
- Highlight:
  - OKE Node Pools config
  - PostgreSQL shape, version
  - Streaming configuration (e.g., brokers, replication, mm2)
  - Object Storage for backups or Helm registry

---

### 18. Security Considerations
- IAM Policy examples
- NSG configuration
- Data encryption approach
- Audit logs or Logging Analytics setup

---

### 19. High Availability & Disaster Recovery
- OKE NodePools across ADs
- PostgreSQL HA with replica
- Object Storage cross-region replication
- DNS failover via Traffic Management
- DR architecture summary

---

### 20. Closing Feedback
- Placeholder for feedback from:
  - Oracle
  - {datos['cliente']}

---

### 21. Sign-Off Section
- Client Acceptance
- Oracle Confirmation
- Final next steps
- Version tagging

---

### Technical & Formatting Requirements

1. Use **exact OCI service names**: {', '.join(datos['servicios_oci'])}
2. Add **3–5 technical specs per service**
3. Address **security, HA, and scalability**
4. Format using:
   - **Markdown syntax**
   - Tables for specs and milestones
   - **Bold** key terms
   - Bullet points for lists
   - Level 1 and 2 headings consistently
5. Use current date for generated content

---

Generate complete, realistic, technically accurate content for each section to build a professional SOW for OCI validation of **{datos['proyecto']}** at **{datos['cliente']}**, aligned with Oracle best practices and delivery format.
"""




    prompt = f"""
Generate a comprehensive Oracle Cloud Infrastructure (OCI) Application Validation document for client {datos['cliente']} using the following OCI services: {', '.join(datos['servicios_oci'])}.


Follow this exact structure and include all specified sections:

1. **Document Header**
- ISV: [Legal Company Name]
- Application: [Product Name]
- Type: Statement of Work
- Date: [Current Date]
- Version: [Version Number]
- Confidentiality disclaimer

2. **Version History Table**
- 3-5 version entries showing evolution
- Include version, date, author, description

3. **Project Status**
- Current phase (Planning/Implementation/Validation)
- Next 3 critical actions with owners

4. **Participant Table**
- Oracle team members to be filled
- Client team members to be filled
- Include names, titles, emails

5. **Project Summary**
- Client business overview (1 paragraph)
- Application purpose (1 paragraph)
- Key technologies (bulleted list)
- OCI services being implemented (section highlighting {', '.join(datos['servicios_oci'])})

6. **Scope Definition**
- In-scope components (bulleted list)
- Out-of-scope items (bulleted list)
- Validation boundaries

7. **Milestone Timeline**
- 5-7 key milestones
- Dates, completion status, dependencies
- Include OCI service implementation phases

8. **Validation Criteria**
- Technical metrics table (performance, availability)
- Security requirements
- Compliance checks

9. **Architecture Sections**
Current Environment:
- Diagram description
- Technology stack
- Pain points

OCI Target Architecture:
- Services diagram ({', '.join(datos['servicios_oci'])} integration)
- Component mapping
- Migration approach

10. **Implementation Plan**
- Configuration details for {datos['servicios_oci'][0]} and other services
- Security settings
- Monitoring setup

11. **Sign-off Section**
- Client acceptance criteria
- Oracle validation approval
- Next steps post-validation

Technical Requirements:
1. Use exact OCI service names: {', '.join(datos['servicios_oci'])}
2. Include 3-5 technical specifications per service
3. Cover security configurations
4. Address scalability considerations
5. Use current dates

Formatting Rules:
- Markdown syntax
- Tables for comparative data
- Bullet points for lists
- Bold for key terms
- Consistent heading levels

Generate complete, technically accurate content for all sections, focusing on practical implementation of {', '.join(datos['servicios_oci'])} for {datos['cliente']}'s environment.

The summary , scope and expectations of the PoC are the following : - Validation Description: {datos['descripcion_validacion']}
"""


    resultado = generate_chat_llama(prompt2)
    texto_generado = resultado["response"]  # ✅ Accede al texto

    resumen = texto_generado.split("##")[0].strip()
    detalles = "\n".join(texto_generado.split("##")[1:]).strip()

    env = Environment(loader=FileSystemLoader("."))
    plantilla = env.get_template("plantilla.sow.md.j2")
     # Carga plantilla Word
   # doc = DocxTemplate("Application_Validation_Template.docx")



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
    subprocess.run(["pandoc", f"{nombre_base}.md", "-o", nombre_archivo])
    return nombre_archivo

