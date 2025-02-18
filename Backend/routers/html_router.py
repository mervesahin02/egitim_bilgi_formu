from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from Backend.services.html_generator import generate_html_from_data

import os

router = APIRouter(prefix="/html", tags=["HTML"])

@router.get("/download/{file_name}")
async def download_html(file_name: str):
    """
    Kullanıcının yüklediği ve dönüştürülen HTML dosyasını indirir.
    """
    file_path = f"output/{file_name}.html"
    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        raise HTTPException(status_code=404, detail="Dosya bulunamadı.")
