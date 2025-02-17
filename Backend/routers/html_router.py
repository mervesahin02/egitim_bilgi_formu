import os
from fastapi import APIRouter, HTTPException, File, UploadFile
from fastapi.responses import FileResponse
from services.html_generator import generate_html_from_data
import json

router = APIRouter(prefix="/html", tags=["HTML"])

@router.post("/generate")
async def generate_html(data: dict):
    """
    JSON verisi alır, şablonla birleştirir ve HTML dosyasını oluşturur.
    """
    try:
        # HTML dosyasını oluştur
        output_file = generate_html_from_data(data, template_path="egitim_bilgi_formu.html", output_dir="output")
        # Dosya yolunu döndür
        return {"message": f"HTML dosyası başarıyla oluşturuldu: {output_file}", "file_path": output_file}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"HTML oluşturulurken bir hata oluştu: {str(e)}")

@router.get("/download/{file_name}")
async def download_file(file_name: str):
    """
    Oluşturulmuş HTML dosyasını indir.
    """
    file_path = f"output/{file_name}.html"
    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        raise HTTPException(status_code=404, detail="Dosya bulunamadı.")
