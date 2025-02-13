from docx import Document
from thefuzz import fuzz, process  # Fuzzy string matching için

def find_best_match(key, choices, threshold=60):  # isim benzerliği olan keyleri eşleştiriyor
    best_match, score = process.extractOne(key, choices, scorer=fuzz.token_sort_ratio)
    return best_match if score >= threshold else None

def read_docx(file_path):
    doc = Document(file_path)

    data = {
        "egitim_adi": "",
        "egitmen_adi": "",
        "egitim_suresi": "",
        "hedef_kitle": "",
        "egitim_ozeti": "",
        "kaynak_dokumanlar": "",
        "id": ""
    }

    for table in doc.tables:
        for row in table.rows:
            if len(row.cells) >= 2:
                key_text = row.cells[0].text.strip()
                value_text = row.cells[1].text.strip()

                if key_text:
                    best_match = find_best_match(key_text, data.keys())
                    if best_match:
                        data[best_match] = value_text

    for key in data:
        if not data[key]:
            data[key] = "Veri Yok"
    
    return data
