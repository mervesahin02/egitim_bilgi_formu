from docx import Document
from io import BytesIO  # BytesIO import et
from thefuzz import fuzz, process  # Fuzzy string matching için

import traceback  # Hata yönetimi için traceback ekle
from Backend.services.data_validator import find_best_match

def read_docx(file):
    """DOCX dosyasını okur ve JSON formatında döndürür."""
    try:
        doc = Document(BytesIO(file))  # ✅ `BytesIO` ile `bytes` nesnesini `file-like` objeye dönüştür

        data = {
            "egitim_adi": "",
            "egitmen_adi": "",
            "egitim_suresi": "",
            "hedef_kitle": "",
            "egitim_ozeti": "",
            "kaynak_dokumanlar": "",
            "id": ""
        }

        print("\n🔍 DOCX Dosyası Okunuyor...")
        print("📄 Tüm Paragraflar:", [p.text for p in doc.paragraphs])  # Debug için

        for table in doc.tables:
            print("\n📌 TABLO BULUNDU!")  # Yeni tablo bulunduğunda log ekle
            for row in table.rows:
                if len(row.cells) >= 2:
                    key_text = row.cells[0].text.strip()
                    value_text = row.cells[1].text.strip()

                    if key_text:
                        best_match = find_best_match(key_text, data.keys())
                        if best_match:
                            data[best_match] = value_text
                            print(f"✅ EŞLEŞTİ: {key_text} -> {best_match} : {value_text}")  # ✅ Debug log

        for key in data:
            if not data[key]:
                data[key] = "Veri Yok"

        print("\n📊 Okunan Veri:", data)  # JSON çıktısını göster
        return data

    except Exception as e:
        error_message = f"DOCX işleme hatası: {str(e)}\n{traceback.format_exc()}"
        print(error_message)  # Hata mesajını terminalde göster
        raise Exception(error_message)
