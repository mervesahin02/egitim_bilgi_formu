import pdfkit
import os
import traceback

def generate_pdf():
    """
    Görünen HTML sayfasını alır ve PDF'ye çevirir.
    """
    try:
        print("PDF oluşturma işlemi başlatılıyor...")

        # 📌 1️⃣ HTML Çıktı Dosyasını Belirle
        html_path = os.path.join(os.getcwd(), "output", "updated_egitim_cikti.html")  # veya temp_egitim_cikti.html


        if not os.path.exists(html_path):
            raise FileNotFoundError(f" HTML dosyası bulunamadı: {html_path}")

        # 📌 2️⃣ PDF Çıktı Dosyasını Belirle
        pdf_output_path = os.path.join(os.getcwd(), "output", "egitim_bilgileri.pdf")
        os.makedirs("output", exist_ok=True)

        # 📌 3️⃣ PDF Dönüştürme İşlemi
        pdfkit.from_file(html_path, pdf_output_path)

        print(f"PDF başarıyla oluşturuldu: {pdf_output_path}")
        return pdf_output_path

    except Exception as e:
        error_message = f"🚨 PDF oluşturma hatası: {str(e)}\n{traceback.format_exc()}"
        print(error_message)
        raise Exception(error_message)

