from docx_reader import read_docx
from html_generator import generate_html_from_data
from log_utils import log_message, log_input
from data_validator import prompt_for_missing_data

def init():
    docx_path = log_input('Lütfen .docx dosyasının yolunu girin: ').strip('"')
    log_message("DOCX dosyası okunuyor...")
    template_path = "egitim_bilgi_formu.html"
    output_dir = "output"

    log_message("DOCX dosyası okunuyor...")
    data = read_docx(docx_path)
    data = prompt_for_missing_data(data)
    log_message(data)

    log_message("HTML oluşturuluyor...")
    output_file = generate_html_from_data(data, template_path, output_dir)

    log_message(f"HTML dosyası oluşturuldu: {output_file}")

if __name__ == "__main__":
    init()
