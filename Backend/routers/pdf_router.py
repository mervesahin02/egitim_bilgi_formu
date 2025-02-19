from fastapi import APIRouter, HTTPException
from Backend.services.pdf_generator import generate_pdf

router = APIRouter(prefix="/pdf", tags=["PDF"])

@router.post("/generate")
async def generate_pdf_endpoint(data: dict):
    """
    JSON verisini alır, PDF'e çevirir ve indirilebilir URL döndürür.
    """
    try:
        pdf_path = generate_pdf(data)
        return {"message": "PDF başarıyla oluşturuldu!", "pdf_url": f"http://127.0.0.1:8001/pdf/download"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/download")
async def download_pdf():
    """
    PDF dosyasını indirmek için endpoint.
    """
    from fastapi.responses import FileResponse
    pdf_path = "output/egitim_bilgileri.pdf"
    
    if not os.path.exists(pdf_path):
        raise HTTPException(status_code=404, detail="PDF bulunamadı!")
    
    return FileResponse(pdf_path, media_type='application/pdf', filename="egitim_bilgileri.pdf")
