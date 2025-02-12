import os
from docx import Document
from jinja2 import Environment, FileSystemLoader
from thefuzz import fuzz, process  # Fuzzy string matching için

def find_best_match(key, choices, threshold=60):  # Önceden 80'di
    best_match, score = process.extractOne(key, choices, scorer=fuzz.token_sort_ratio)
    return best_match if score >= threshold else None

# .docx dosyasını okuma fonksiyonu
def read_docx(file_path):
    doc = Document(file_path)

    data = {
        "egitim_adi": "",
        "egitmen_adi": "",
        "egitim_suresi": "",
        "teslim_tarihi": "",
        "egitim_amaci": "",
        "egitim_seviyesi": "",
        "egitim_niteligi": "",
        "egitim_gereksinimleri": "",
        "hedef_kitle": "",
        "egitim_ozeti": "",
        "sikca_sorulan_sorular": ""
    }

    # **Tabloyu işleyelim (Artık her satırın ilk hücresini key, ikinci hücresini value olarak alıyoruz)**
    for table in doc.tables:
        for row in table.rows:
            if len(row.cells) >= 2:  # En az iki hücre olmalı (Key - Value)
                key_text = row.cells[0].text.strip()  # Sol hücre (Key)
                value_text = row.cells[1].text.strip()  # Sağ hücre (Value)

                if key_text:  # Boş başlıkları atla
                    best_match = find_best_match(key_text, data.keys())  # Key'i eşleştir
                    if best_match:
                        data[best_match] = value_text  # Doğru key'e karşılık gelen değeri ata

    # Eğer bazı değerler boşsa, "Veri Yok" yap
    for key in data:
        if not data[key]:  # Eğer değer boşsa
            data[key] = "Veri Yok"
    
    return data

# HTML oluşturma fonksiyonu
def generate_html_from_data(data, template_path, output_dir):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_path)
    
    os.makedirs(output_dir, exist_ok=True)

    egitim_adi = str(data['egitim_adi']).replace(' ', '_') if data['egitim_adi'] else "default_egitim_adi"
    output_file = os.path.join(output_dir, f"{egitim_adi}.html")

    html_content = template.render(data)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"{output_file} oluşturuldu.")

if __name__ == "__main__":
    docx_path = input('Lütfen .docx dosyasının yolunu girin: ').strip('"')
    template_path = "egitim_bilgi_formu.html"
    output_dir = "output"

    data = read_docx(docx_path)  # .docx dosyasından verileri al

    generate_html_from_data(data, template_path, output_dir)  # HTML oluştur
