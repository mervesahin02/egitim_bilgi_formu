
# Eğitim Bilgi Sistemi - Backend  

Bu proje, eğitim bilgilerini içeren bir sistemin **FastAPI** ile geliştirilmiş backend tarafını içermektedir. Kullanıcılar `.DOCX` dosyalarını yükleyebilir, eksik verileri kontrol edebilir, HTML çıktıları oluşturabilir ve PDF/Word dosyalarına dönüştürebilir.  

## 🚀 Teknolojiler  

- **FastAPI** → RESTful API geliştirme  
- **Python** → Backend için temel dil  
- **Jinja2** → HTML şablonları oluşturma  
- **pdf2docx** → PDF'den Word'e çevirme  
- **python-docx** → `.DOCX` dosyalarını okuma  
- **TheFuzz** → Metin benzerliği analizi (Fuzzy Matching)  
- **Uvicorn** → API sunucusunu çalıştırma  
- **pdfkit** → HTML'den PDF oluşturma  

## 📌 API İçeriği  

### 1️⃣ **DOCX Okuma Modülü (`docx_router.py`)**  
- Kullanıcıların yüklediği `.DOCX` dosyalarını okur ve JSON formatına dönüştürür.  
- **Fuzzy Matching** ile başlıkları tanıyıp ilgili verilere eşleştirir.  

📌 **Örnek Kullanım:**  
```bash
curl -X POST -F "file=@dosya.docx" http://127.0.0.1:8001/docx/read
```
---

### 2️⃣ **Eksik Veri Kontrolü (`data_validator.py`)**  
- JSON içindeki eksik alanları kontrol eder.  
- Gerekirse eksik verileri kullanıcıdan ister.  

📌 **Örnek Çıktı:**  
```json
{
    "eksik_veriler": ["egitim_adi", "egitmen_adi"]
}
```

---

### 3️⃣ **HTML Çıktısı Oluşturma (`html_router.py` ve `html_generator.py`)**  
- JSON verisini alıp **HTML formatına çevirir** ve kaydeder.  

📌 **Örnek Kullanım:**  
```bash
curl -X POST -H "Content-Type: application/json" -d '{"egitim_adi": "Python Kursu"}' http://127.0.0.1:8001/html/generate
```

---

### 4️⃣ **PDF Dönüştürücü (`pdf_router.py` ve `pdf_generator.py`)**  
- HTML verisini **PDF formatına dönüştürür ve indirilebilir hale getirir**.  

📌 **Örnek Kullanım:**  
```bash
curl -X GET http://127.0.0.1:8001/pdf/download
```

📌 **Kullanılan Teknoloji:** `pdfkit`  
- HTML dosyasını PDF'ye çevirir.  
- Çıktılar **output/egitim_bilgileri.pdf** konumuna kaydedilir.  

---

### 5️⃣ **Word Dönüştürücü (`word_router.py` ve `word_generator.py`)**  
- Kullanıcının yüklediği **PDF dosyasını Word'e çevirir**.  

📌 **Örnek Kullanım:**  
```bash
curl -X POST -F "file=@dosya.pdf" http://127.0.0.1:8001/word/convert
```

📌 **Kullanılan Teknoloji:** `pdf2docx`  
- PDF dosyasını `.DOCX` formatına dönüştürür.  
- Çıktılar **output/** klasörüne kaydedilir.  

---

### 6️⃣ **Log Sistemi (`log_router.py` ve `log_utils.py`)**  
- Bilgi, hata ve debug mesajlarını loglar.  

📌 **Örnek Kullanım:**  
```bash
curl -X GET "http://127.0.0.1:8001/log/message?message=Test Log Mesajı"
```

---

## 📂 Dosya Yapısı  

```
📁 backend  
 ├── 📄 main.py                   # FastAPI uygulamasının giriş noktası  
 ├── 📁 routers  
 │   ├── docx_router.py           # DOCX okuma API'si  
 │   ├── html_router.py           # HTML oluşturma API'si  
 │   ├── pdf_router.py            # PDF dönüşümü API'si  
 │   ├── word_router.py           # Word dönüşümü API'si  
 │   ├── log_router.py            # Log işlemleri API'si  
 ├── 📁 services  
 │   ├── data_validator.py        # Eksik veri kontrolü  
 │   ├── docx_reader.py           # DOCX okuma işlemleri  
 │   ├── html_generator.py        # HTML çıktısı oluşturma  
 │   ├── pdf_generator.py         # PDF oluşturma servisi  
 │   ├── word_generator.py        # PDF'den Word oluşturma servisi  
 ├── 📁 utils  
 │   ├── log_utils.py             # Log yönetimi  
 ├── 📁 static                     # Statik dosyalar (CSS, JS vb.)  
```

---

## 🔧 Kurulum ve Çalıştırma  

1️⃣ **Gereksinimleri Yükleyin**  
```bash
pip install fastapi uvicorn python-docx pdf2docx thefuzz jinja2 pdfkit
```

2️⃣ **API'yi Başlatın**  
```bash
uvicorn main:app --reload
```

3️⃣ **API'yi Test Edin**  
Tarayıcınızdan **http://127.0.0.1:8001** adresine giderek API'nin çalıştığını kontrol edebilirsiniz.

---

## 🎯 Gelecekteki Geliştirmeler  

✅ **Daha güçlü veri doğrulama mekanizması**  
✅ **Kullanıcı yetkilendirme (JWT)**  
✅ **Gerçek zamanlı belge işleme (WebSockets)**  

