# Backend/main.py
from fastapi import FastAPI
from routers import docx_router, html_router, log_router

app = FastAPI()

# Router'ları ekle
app.include_router(docx_router.router)  # <-- Burada .router kullanmalısınız
app.include_router(html_router.router)
app.include_router(log_router.router)

@app.get("/")
def root():
    return {"message": "Eğitim Bilgi Formu Backend Çalışıyor 🚀"}

# FastAPI'yi Uvicorn ile başlatmak için
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
