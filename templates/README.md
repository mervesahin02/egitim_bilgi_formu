
# Eğitim Bilgi Sistemi - Frontend  

Bu proje, eğitim bilgilerini içeren bir sistemin frontend tarafını içermektedir. Kullanıcılar, `.DOCX` dosyalarını yükleyerek eğitim bilgilerini görüntüleyebilir, eksik bilgileri tamamlayabilir ve çıktı alabilir.  

## 📌 Proje İçeriği  

### 1️⃣ **Eğitim Bilgi Formu (`egitim_bilgi_formu.html`)**  
Kullanıcıların `.DOCX` formatındaki eğitim bilgilerini yüklemeleri için oluşturulmuş bir arayüzdür.  

- `.DOCX` dosyası yükleme  
- Şık ve kullanıcı dostu tasarım  

### 2️⃣ **Eksik Veri Formu (`eksik_veri_formu.html`)**  
Eğitim bilgileri eksik olduğunda, kullanıcıların eksik alanları doldurmasını sağlayan bir form içerir.  

- Eksik eğitim bilgilerini tamamlayabilme  
- Form alanları: Eğitim Adı, Eğitmen, Süre, Özet, Hedef Kitle vb.  

### 3️⃣ **Eğitim Çıktı Sayfası (`egitim_cikti.html`)**  
Yüklenen ve düzenlenen eğitim bilgilerini kullanıcıya PDF veya Word olarak çıktı alma imkanı sunan sayfadır.  

- Eğitim bilgilerini düzenli bir formatta görüntüleme  
- HTML sayfasını **PDF'ye çevirme**  
- Eğitim bilgisini **Word formatına dönüştürme**  

### 4️⃣ **PDF'den Word'e Dönüştürme (`pdf2docx.html`)**  
Kullanıcıların PDF dosyalarını `.DOCX` formatına çevirmelerine olanak tanır.  

- Kullanıcı tarafından PDF yüklenir  
- PDF, **Word formatına çevrilerek indirilebilir**  

## 🚀 Teknolojiler  

- **HTML, CSS, JavaScript**  
- **html2pdf.js** → PDF çıktısı oluşturma  
- **Fetch API** → PDF-Word dönüşümü için backend ile iletişim  

## 📂 Dosya Yapısı  


📁 frontend\
├── 📄 egitim\_bilgi\_formu.html   # .DOCX dosyası yükleme sayfası\
├── 📄 eksik\_veri\_formu.html     # Eksik eğitim bilgilerini girme sayfası\
├── 📄 egitim\_cikti.html         # Eğitim detaylarını görüntüleme & çıktı alma\
├── 📄 pdf2docx.html             # PDF'den Word'e çevirme\
├── 📁 js\
│   ├── main.js                 # Ana JavaScript dosyası\
├── 📁 assets\
│   ├── logo.png                # Sayfa içinde kullanılan logolar



## 📌 Kurulum ve Kullanım  

1️⃣ **Projeyi Çalıştırma**  
- Proje dosyalarını bir web sunucusunda çalıştırabilir veya doğrudan tarayıcınızda açabilirsiniz.  

2️⃣ **Gereksinimler**  
- Tarayıcınızda **JavaScript etkin** olmalıdır.  
- `.DOCX` ve `.PDF` işlemleri için **backend servisi çalışmalıdır**.  

3️⃣ **Kullanım Adımları**  
- `.DOCX` dosyanızı **egitim_bilgi_formu.html** üzerinden yükleyin.  
- Eksik bilgiler varsa **eksik_veri_formu.html** sayfasında tamamlayın.  
- **egitim_cikti.html** sayfasında eğitim bilgilerini görüntüleyin ve PDF/Word olarak kaydedin.  
- PDF'den Word'e çevirmek için **pdf2docx.html** sayfasını kullanın.  

## 🎯 Gelecekteki Geliştirmeler  

✅ **Daha gelişmiş UI tasarımı**  
✅ **Backend API entegrasyonu ile gerçek zamanlı veri kaydı**  
✅ **Daha fazla dosya formatı desteği (Excel, JSON vb.)**  
