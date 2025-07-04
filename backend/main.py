from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import FileResponse, JSONResponse
from generator import generar_documento
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

@app.post("/generar")
async def generar(request: Request):
    datos = await request.json()
    try:
        ruta_docx = generar_documento(datos)
        return FileResponse(
            ruta_docx,
            filename="documento.docx",
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
