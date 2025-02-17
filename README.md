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

