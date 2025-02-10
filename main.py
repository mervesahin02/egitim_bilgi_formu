import os
import pandas as pd
from jinja2 import Environment, FileSystemLoader
from docx import Document

def docx_to_csv(docx_path, csv_path):
    # DOCX dosyasını aç
    doc = Document(docx_path)
    
    # Başlıklar ve içerikler
    data = {
        "Eğitmenin Adı-Soyadı": "",
        "Eğitimin Adı": "",
        "Tahmini Eğitim Süresi": "",
        "Tahmini Eğitim Teslim Tarihi": "",
        "Eğitimin Amacı": "",
        "Eğitim Seviyesi": "",
        "Eğitim Niteliği": "",
        "Eğitim Gereksinimleri": "",
        "Hedef Kitle": "",
        "Eğitim Özeti": "",
        "Sıkça Sorulan Sorular": ""
    }
    
    # DOCX'ten verileri al
    for para in doc.paragraphs:
        # Her paragrafa bakıp verileri yerleştir
        if "Eğitmenin Adı-Soyadı" in para.text:
            data["Eğitmenin Adı-Soyadı"] = para.text.split(":")[1].strip()
        elif "Eğitimin Adı" in para.text:
            data["Eğitimin Adı"] = para.text.split(":")[1].strip()
        elif "Tahmini Eğitim Süresi" in para.text:
            data["Tahmini Eğitim Süresi"] = para.text.split(":")[1].strip()
        elif "Tahmini Eğitim Teslim Tarihi" in para.text:
            data["Tahmini Eğitim Teslim Tarihi"] = para.text.split(":")[1].strip()
        elif "Eğitimin Amacı" in para.text:
            data["Eğitimin Amacı"] = para.text.split(":")[1].strip()
        elif "Eğitim Seviyesi" in para.text:
            data["Eğitim Seviyesi"] = para.text.split(":")[1].strip()
        elif "Eğitim Niteliği" in para.text:
            data["Eğitim Niteliği"] = para.text.split(":")[1].strip()
        elif "Eğitim Gereksinimleri" in para.text:
            data["Eğitim Gereksinimleri"] = para.text.split(":")[1].strip()
        elif "Hedef Kitle" in para.text:
            data["Hedef Kitle"] = para.text.split(":")[1].strip()
        elif "Eğitim Özeti" in para.text:
            data["Eğitim Özeti"] = para.text.split(":")[1].strip()
        elif "Sıkça Sorulan Sorular" in para.text:
            data["Sıkça Sorulan Sorular"] = para.text.split(":")[1].strip()

    # CSV'ye yaz
    df = pd.DataFrame([data])  # Tek satır veri
    df.to_csv(csv_path, index=False, encoding="utf-8")
    print(f"{csv_path} dosyası oluşturuldu.")

def generate_html_from_csv(csv_path, template_path, output_dir):
    # CSV'yi oku
    df = pd.read_csv(csv_path)
    
    # Jinja2 ortamını ayarla (templates klasöründen şablonları yükle)
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_path)

    # Çıktı klasörünü oluştur
    os.makedirs(output_dir, exist_ok=True)

    # CSV'deki her satır için HTML oluştur
    for _, row in df.iterrows():
        data = {
            "egitim_adi": row.get("Eğitimin Adı", ""),
            "egitmen_adi": row.get("Eğitmenin Adı-Soyadı", ""),
            "egitim_suresi": row.get("Tahmini Eğitim Süresi", ""),
            "teslim_tarihi": row.get("Tahmini Eğitim Teslim Tarihi", ""),
            "egitim_amaci": row.get("Eğitimin Amacı", ""),
            "egitim_seviyesi": row.get("Eğitim Seviyesi", ""),
            "egitim_niteligi": row.get("Eğitim Niteliği", ""),
            "egitim_gereksinimleri": row.get("Eğitim Gereksinimleri", ""),
            "hedef_kitle": row.get("Hedef Kitle", ""),
            "egitim_ozeti": row.get("Eğitim Özeti", ""),
            "sikca_sorulan_sorular": row.get("Sıkça Sorulan Sorular", "")
        }

        # HTML oluştur
        html_content = template.render(data)

        # Çıktıyı dosyaya yaz
        output_file = os.path.join(output_dir, f"{data['egitim_adi'].replace(' ', '_')}.html")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html_content)

        print(f"{output_file} oluşturuldu.")

if __name__ == "__main__":
    # Kullanıcıdan dosya yolu al
    docx_path = input("Lütfen .docx dosyasının yolunu girin: ")
    
    # DOCX'i CSV'ye dönüştür
    csv_path = "egitim_bilgileri.csv"
    docx_to_csv(docx_path, csv_path)
    
    # Şablon ve çıktı dizini
    template_path = "egitim_bilgi_formu.html"
    output_dir = "output"
    
    # CSV'den HTML'ye dönüştür
    generate_html_from_csv(csv_path, template_path, output_dir)
