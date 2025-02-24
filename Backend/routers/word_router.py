from fastapi import APIRouter
from fastapi.responses import FileResponse
from Backend.services.word_generator import generate_word

router = APIRouter(prefix="/word", tags=["Word"])

@router.post("/generate")
async def create_word(data: dict):
    """
    JSON verisini alır ve Word dosyası oluşturur.
    """
    word_path = generate_word(data)
    
    # Dosyayı indirmek için FileResponse döndür
    return FileResponse(word_path, media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document", filename="egitim_bilgileri.docx")
