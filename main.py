import os
import pandas as pd
from docx import Document

def fill_form(template_path, output_path, data):
    doc = Document(template_path)

    for paragraph in doc.paragraphs:
        for key in data:
            if key in paragraph.text:
                for run in paragraph.runs:
                    run.text = run.text.replace(key, data[key])

    doc.save(output_path)

def generate_docxs_from_csv(csv_path, template_path):
    df = pd.read_csv(csv_path)

    for idx, row in df.iterrows():
        data = {
            '[Eğitmenin Adı-Soyadı]': row.get('Eğitmenin Adı-Soyadı', ''),
            '[Eğitimin Adı]': row.get('Eğitimin Adı', ''),
            '[Tahmini Eğitim Süresi]': row.get('Tahmini Eğitim Süresi', ''),
            '[Tahmini Eğitim Teslim Tarihi]': row.get('Tahmini Eğitim Teslim Tarihi', ''),
            '[Eğitimin Amacı]': row.get('Eğitimin Amacı', ''),
            '[Eğitim Seviyesi]': row.get('Eğitim Seviyesi', ''),
            '[Eğitim Niteliği]': row.get('Eğitim Niteliği', ''),
            '[Eğitim Gereksinimleri]': row.get('Eğitim Gereksinimleri', ''),
            '[Hedef Kitle]': row.get('Hedef Kitle', ''),
            '[Eğitim Özeti]': row.get('Eğitim Özeti', ''),
            '[Kullanılacak Programlar]': row.get('Kullanılacak Programlar', ''),
            '[Sıkça Sorulan Sorular(SSS) & Cevapları]': row.get('Sıkça Sorulan Sorular(SSS) & Cevapları', '')
        }
        output_path = f"{data['[Eğitimin Adı]'].replace(' ', '_')}.docx"

        # Dosya zaten varsa, eskiyi silip yenisini kaydet
        if os.path.exists(output_path):
            os.remove(output_path)

        fill_form(template_path, output_path, data)

if __name__ == '__main__':
    template_path = 'first_form.docx'
    csv_path = 'egitim_bilgileri.csv'
    generate_docxs_from_csv(csv_path, template_path)
