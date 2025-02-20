from jinja2 import Environment, FileSystemLoader
import os

# 📌 Jinja2 ortamını ayarla (Doğru şablonu yükle!)
env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("egitim_cikti.html")  # 🔴 Yanlış şablon kullanma, çıktı için doğru olanı seç!

def generate_html_from_data(veri):
    """
    Verilen JSON verisini kullanarak HTML çıktısı oluşturur ve kaydeder.
    """
    try:
        # 📌 HTML çıktısını oluştur
        html_output = template.render(veri)

        # 📌 Dosyanın kaydedileceği yolu belirle
        output_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(output_dir, exist_ok=True)  # ✅ Eğer "output" klasörü yoksa oluştur

        output_path = os.path.join(output_dir, "updated_egitim_cikti.html")

        # 📌 HTML çıktısını kaydet
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html_output)

        print(f"✅ HTML dosyası başarıyla oluşturuldu: {output_path}")  # 🟢 Debug log eklendi
        return output_path  # HTML dosyasının yolunu döndür

    except Exception as e:
        print(f"🚨 HTML oluşturma hatası: {str(e)}")
        raise Exception(f"HTML oluşturma hatası: {str(e)}")
