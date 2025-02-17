import os
from jinja2 import Environment, FileSystemLoader, TemplateNotFound

def generate_html_from_data(data, template_path="egitim_bilgi_formu.html", output_dir="output"):
    # Template path'i doğru şekilde kontrol et ve yol oluştur
    templates_dir = 'templates'
    env = Environment(loader=FileSystemLoader(templates_dir))
    
    try:
        # Şablonu yükle
        template = env.get_template(template_path)
    except TemplateNotFound:
        raise FileNotFoundError(f"Template '{template_path}' bulunamadı.")
    
    # Çıktı dizini oluştur
    os.makedirs(output_dir, exist_ok=True)

    # Eğitim adıyla dosya adını oluştur
    egitim_adi = str(data['egitim_adi']).replace(' ', '_') if data['egitim_adi'] else "default_egitim_adi"
    output_file = os.path.join(output_dir, f"{egitim_adi}.html")

    # HTML içeriğini şablondan oluştur
    html_content = template.render(data)

    # HTML dosyasını yaz
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    return output_file
