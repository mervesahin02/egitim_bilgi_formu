from jinja2 import Environment, FileSystemLoader
import os

# Jinja2 ortamını ayarla
env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("egitim_bilgi_formu.html")

def generate_html_from_data(veri):
    """
    Verilen JSON verisini kullanarak HTML çıktısı oluşturur ve kaydeder.
    """
    # HTML çıktısını oluştur
    html_output = template.render(veri)

    # HTML çıktısını kaydet
    output_path = os.path.join("templates", "output.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_output)

    print("✅ HTML dosyası başarıyla oluşturuldu!")
    return output_path  # HTML dosyasının yolunu döndür

