from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", style='B', size=14)
        self.cell(200, 10, "Eğitim Bilgi Formu", ln=True, align='C')
        self.ln(10)

def generate_pdf(data):
    """
    JSON verisini PDF formatında kaydeder ve dosya yolunu döndürür.
    """
    pdf = PDF()
    pdf.add_page()
    
    # ✅ UTF-8 destekli font ekle
    pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
    pdf.set_font("DejaVu", "", 12)

    for key, value in data.items():
        # Eğer veri 'Veri Yok' ise onu boş string yap
        clean_value = value if value != "Veri Yok" else ""
        pdf.cell(0, 10, f"{key}: {clean_value}", ln=True)

    pdf_output_path = "output/egitim_bilgileri.pdf"
    
    os.makedirs("output", exist_ok=True)  # PDF için klasör oluştur
    pdf.output(pdf_output_path, "F")

    return pdf_output_path
