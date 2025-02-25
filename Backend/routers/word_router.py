from fastapi import APIRouter, Form
from fastapi.responses import FileResponse
from pathlib import Path
from Backend.services.word_generator import generate_word

router = APIRouter(prefix="/word", tags=["Word"])

@router.post("/generate")
async def create_word(pdf_path: str = Form(...)):
    """
    PDF dosyasının yolunu alır ve Word dosyası oluşturur.
    """
    # PDF dosyasının yolunu al
    word_path = generate_word(pdf_path)
    
    # Dosyayı indirmek için FileResponse döndür
    return FileResponse(
        word_path,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        filename="egitim_bilgileri.docx"
    )
