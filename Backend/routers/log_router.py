from fastapi import APIRouter
from datetime import datetime

router = APIRouter(prefix="/log", tags=["Log"])

# Basit loglama endpointi
@router.get("/message")
def log_message(message: str):
    log_entry = f"[{datetime.now()}] - {message}"
    print(log_entry)  # Konsola log yazdırma
    return {"message": log_entry}

# Farklı türde loglar eklemek isterseniz, buraya ekleyebilirsiniz
@router.get("/info")
def log_info(message: str):
    log_entry = f"[INFO] [{datetime.now()}] - {message}"
    print(log_entry)
    return {"message": log_entry}

@router.get("/error")
def log_error(message: str):
    log_entry = f"[ERROR] [{datetime.now()}] - {message}"
    print(log_entry)
    return {"message": log_entry}
