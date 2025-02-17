import logging

# Loglama için bir dosya oluşturuyoruz
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s", handlers=[logging.FileHandler("app.log"), logging.StreamHandler()])

def log_message(message):
    """
    Mesajı hem ekrana hem de log dosyasına yazdırır.
    """
    logging.info(message)
    print(f"[LOG]: {message}")

# API tarafında input almak mümkün olmadığı için, bu fonksiyon kaldırılabilir.
# Kullanıcıdan veri almak için frontend veya endpoint kullanmak gerekebilir.
def log_input(prompt):
    """
    Terminal üzerinden kullanıcıdan veri alır (sadece terminalde çalıştırılacak).
    """
    return input(f"[INPUT]: {prompt}")
