import os
import pandas as pd
from jinja2 import Environment, FileSystemLoader

def generate_html_from_csv(csv_path, template_path, output_dir):
    # CSV'yi oku
    df = pd.read_csv("egitim_bilgileri.csv")
    
    # CSV'nin sütun başlıklarını göster
    print("CSV'deki sütun başlıkları:", df.columns)

    # Boş olan sütunları göster
    print("Eksik veri sayısı:")
    print(df.isnull().sum())

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
    csv_path = "egitim_bilgileri.csv"
    template_path = "egitim_bilgi_formu.html"
    output_dir = "output"
    
    generate_html_from_csv(csv_path, template_path, output_dir)
