import os
from fastapi import FastAPI
from Backend.routers import docx_router, html_router, log_router

app = FastAPI()

# Router'ları ekle
app.include_router(docx_router.router)
app.include_router(html_router.router)
app.include_router(log_router.router)

@app.get("/")
def root():
    return {"message": "Eğitim Bilgi Formu Backend Çalışıyor 🚀"}

if __name__ == "__main__":
    import uvicorn
    
    # Kullanıcıdan dosya yolu al
    file_path = input("Lütfen dönüştürmek istediğiniz .docx dosyasının tam yolunu girin: ")

    # Dosyanın var olup olmadığını kontrol et
    if os.path.exists(file_path) and file_path.endswith(".docx"):
        print(f"✅ Dosya bulundu: {file_path}")
    else:
        print("❌ Geçersiz dosya yolu! Lütfen doğru bir .docx dosyası girin.")
        exit(1)  # Hatalı giriş olursa programı durdur

    uvicorn.run("Backend.services.main:app", host="127.0.0.1", port=8000, reload=True)
