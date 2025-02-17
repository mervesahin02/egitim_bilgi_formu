# Backend/routers/docx_router.py
from fastapi import APIRouter, UploadFile, File
from services.docx_reader import read_docx
from io import BytesIO

router = APIRouter(prefix="/docx", tags=["DOCX"])

@router.post("/read")
async def read_uploaded_docx(file: UploadFile = File(...)):
    # Kullanıcıdan gelen dosyayı al
    content = await file.read()

    # Byte veri olarak DOCX dosyasını işle
    docx_data = read_docx(BytesIO(content))

    return {"parsed_data": docx_data}
