from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from Backend.services.pdf_generator import generate_pdf
import os

router = APIRouter(prefix="/pdf", tags=["PDF"])

@router.post("/generate")
async def generate_pdf_endpoint():
    """
    Son oluşan HTML'yi PDF olarak kaydeder.
    """
    try:
        print("📥 PDF oluşturma isteği alındı...")
        pdf_path = generate_pdf()

        if not os.path.exists(pdf_path):
            raise HTTPException(status_code=500, detail="❌ PDF oluşturulamadı!")

        return {"message": "✅ PDF başarıyla oluşturuldu!", "pdf_url": f"http://127.0.0.1:8001/pdf/download"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"🚨 Hata: {str(e)}")

@router.get("/download")
async def download_pdf():
    pdf_path = "output/egitim_bilgileri.pdf"

    if not os.path.exists(pdf_path):
        raise HTTPException(status_code=404, detail="❌ PDF bulunamadı!")

    return FileResponse(pdf_path, media_type='application/pdf', filename="egitim_bilgileri.pdf")
