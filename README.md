Eğitim Bilgi Formu Uygulaması
=============================

Bu proje, eğitim bilgi formu verilerini DOCX dosyasından alarak HTML formatına dönüştürmeyi amaçlayan bir Python uygulamasıdır. Uygulama, verileri .docx dosyasından okur, eksik verileri kontrol eder ve kullanıcıya eksik verileri manuel olarak doldurabilme seçeneği sunar. Ardından, verileri kullanarak bir HTML sayfası oluşturur.

Başlangıç
---------

Bu uygulama, DOCX dosyasındaki eğitim bilgilerini alır, eksik verileri kontrol eder, eksik olanları kullanıcıya sorar ve son olarak verileri kullanarak bir HTML sayfası oluşturur. Bu sayfa, eğitim bilgilerini şık bir şekilde görüntüler ve çıktıyı bir dosya olarak kaydeder.

Özellikler
----------

-   `.docx` dosyasından eğitim bilgilerini çıkarma
-   Eksik verileri tespit etme ve kullanıcıya manuel olarak doldurma imkanı verme
-   Verilerle HTML sayfası oluşturma
-   `Jinja2` şablon motoru kullanarak dinamik HTML oluşturma
-   Verilerinizi yerel dosya sisteminizde kaydedebilme
-   Kullanıcı dostu giriş ve çıkış logları


Kullanım
--------

1.  `main.py` dosyasını çalıştırarak uygulamayı başlatın:

```
python main.py

```

1.  Program, `.docx` dosyasının yolunu girmenizi isteyecek. Dosyanın yolunu girin ve `Enter` tuşuna basın.

2.  Program, DOCX dosyasındaki verileri okur ve eksik verileri kontrol eder. Eksik veri bulunursa, eksik verileri manuel olarak girmeniz istenecektir.

3.  Veriler eksiksiz hale geldikten sonra, HTML dosyası oluşturulacak ve belirtilen çıkış dizinine kaydedilecektir.

- 1. Ekran

![WhatsApp Görsel 2025-05-28 saat 10 35 04_b427b511](https://github.com/user-attachments/assets/189a9651-93ab-4eb1-90f5-5fbb35f2d716)

- 2. Ekran
![WhatsApp Görsel 2025-05-28 saat 10 35 18_950fa854](https://github.com/user-attachments/assets/b38b58d3-9855-4aba-b301-7c86df4d1a38)
![WhatsApp Görsel 2025-05-28 saat 10 35 35_fb9a0910](https://github.com/user-attachments/assets/45ec64cc-388d-4195-bf4d-b027a9d130fc)
![WhatsApp Görsel 2025-05-28 saat 10 35 44_12d08049](https://github.com/user-attachments/assets/d98d194d-1e6e-4904-91fe-a011f060375b)

- 3. Ekran
![WhatsApp Görsel 2025-05-28 saat 10 36 09_0e6db0d2](https://github.com/user-attachments/assets/4b7f76a3-7307-4145-aa18-4ca94730a73a)
![WhatsApp Görsel 2025-05-28 saat 10 36 16_467fbcf6](https://github.com/user-attachments/assets/3bd26962-b114-4937-ac23-197e10d9959d)

