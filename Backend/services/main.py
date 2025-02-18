import os
from fastapi import FastAPI
from Backend.routers import docx_router, html_router, log_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS'u aktif et
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Tüm kaynaklara izin ver (test amaçlı)
    allow_credentials=True,
    allow_methods=["*"],  # Tüm HTTP metodlarına izin ver
    allow_headers=["*"],  # Tüm başlıklara izin ver
)

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
