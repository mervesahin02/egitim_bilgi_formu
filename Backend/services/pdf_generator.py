import selectpdf
import os

API_KEY = "YOUR_SELECTPDF_API_KEY"  # ✅ SelectPDF API Anahtarını Buraya Gir!

def generate_pdf(data):
    """
    SelectPDF kullanarak JSON verisini PDF'ye çevirir.
    """
    try:
        print("📥 PDF oluşturma işlemi başlıyor...")

        # 📌 1️⃣ HTML Şablonu Dosyasını Yükle
        html_template_path = os.path.join(os.getcwd(), "templates", "egitim_cikti.html")

        if not os.path.exists(html_template_path):
            raise FileNotFoundError(f"❌ HTML şablonu bulunamadı: {html_template_path}")

        with open(html_template_path, "r", encoding="utf-8") as f:
            html_content = f.read()

        # 📌 2️⃣ HTML İçeriğini Güncelle (JSON Verileriyle Doldur)
        html_content = html_content.replace("{{egitim_adi}}", data.get("egitim_adi", "Bilinmiyor"))
        html_content = html_content.replace("{{egitmen_adi}}", data.get("egitmen_adi", "Bilinmiyor"))
        html_content = html_content.replace("{{egitim_suresi}}", data.get("egitim_suresi", "Bilinmiyor"))
        html_content = html_content.replace("{{egitim_ozeti}}", data.get("egitim_ozeti", "Bilinmiyor"))
        html_content = html_content.replace("{{hedef_kitle}}", data.get("hedef_kitle", "Bilinmiyor"))
        html_content = html_content.replace("{{kaynak_dokumanlar}}", data.get("kaynak_dokumanlar", "Bilinmiyor"))

        # 📌 3️⃣ Güncellenmiş HTML'yi Yeni Bir Dosya Olarak Kaydet
        updated_html_path = os.path.join(os.getcwd(), "output", "updated_egitim_cikti.html")
        os.makedirs("output", exist_ok=True)

        with open(updated_html_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        # 📌 4️⃣ SelectPDF Kullanarak HTML Dosyasını PDF'ye Dönüştür
        converter = selectpdf.HtmlToPdfClient(API_KEY)
        pdf_output_path = os.path.join(os.getcwd(), "output", "egitim_bilgileri.pdf")

        # ✅ `convert_local_file()` ile PDF oluştur (Bu metod `convert_string()` yerine çalışır!)
        converter.convert_local_file(updated_html_path, pdf_output_path)

        print(f"✅ PDF başarıyla oluşturuldu: {pdf_output_path}")
        return pdf_output_path

    except Exception as e:
        print(f"🚨 PDF oluşturma hatası: {str(e)}")
        raise Exception(f"PDF oluşturma hatası: {str(e)}")
