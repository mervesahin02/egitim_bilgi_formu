document.addEventListener("DOMContentLoaded", function () {

    // 📌 Dosya yükleme sayfasında mıyız?
    if (document.getElementById("uploadForm")) {
        document.getElementById("uploadForm").addEventListener("submit", async function (event) {
            event.preventDefault();
            let fileInput = document.getElementById("fileInput").files[0];

            if (!fileInput) {
                alert("Lütfen bir .docx dosyası seçin!");
                return;
            }

            let formData = new FormData();
            formData.append("file", fileInput);

            try {
                console.log("📤 Dosya backend’e gönderiliyor...");
                let response = await fetch("http://127.0.0.1:8001/docx/read", {
                    method: "POST",
                    body: formData
                });

                if (!response.ok) {
                    throw new Error("Dosya yükleme başarısız! HTTP Hata: " + response.status);
                }

                let result = await response.json();
                console.log("✅ Backend JSON Yanıtı:", result);

                if (result.parsed_data) {
                    // JSON verisini localStorage’a kaydet
                    localStorage.setItem("egitimData", JSON.stringify(result.parsed_data));

                    // Eksik veri formu sayfasına yönlendir
                    console.log("🟢 Yönlendirme: eksik_veri_formu.html");
                    window.location.href = "eksik_veri_formu.html";
                } else {
                    alert("Hata: Backend JSON verisi boş geldi!");
                }

            } catch (error) {
                console.error("Hata:", error);
                alert("Dosya yükleme başarısız! Hata: " + error.message);
            }
        });
    }

    // 📌 Eksik veri formu sayfasında mıyız?
    if (document.getElementById("missingDataForm")) {
        let savedData = JSON.parse(localStorage.getItem("egitimData") || "{}");

        // Eğer backend boş veri döndürdüyse, kullanıcıya uyarı ver
        if (Object.keys(savedData).length === 0) {
            alert("Hata! Backend'den gelen veri boş.");
            window.location.href = "egitim_bilgi_formu.html";
            return;
        }

        // Form alanlarını otomatik doldur
        document.getElementById("egitimAdi").value = savedData.egitim_adi || "";
        document.getElementById("egitmenAdi").value = savedData.egitmen_adi || "";
        document.getElementById("egitimSuresi").value = savedData.egitim_suresi || "";
        document.getElementById("egitimOzeti").value = savedData.egitim_ozeti || "";
        document.getElementById("hedefKitle").value = savedData.hedef_kitle || "";
        document.getElementById("kaynakDokumanlar").value = savedData.kaynak_dokumanlar || "";

        // Butona tıklanınca formu kaydet ve yönlendir
        document.getElementById("missingDataForm").addEventListener("submit", function (event) {
            event.preventDefault();
            submitForm();
        });
    }

    // 📌 Çıktı sayfasında mıyız?
    if (document.getElementById("outputContainer")) {
        let savedData = JSON.parse(localStorage.getItem("egitimData") || "{}");

        document.getElementById("displayEgitimAdi").textContent = savedData.egitim_adi || "Bilinmiyor";
        document.getElementById("displayEgitmenAdi").textContent = savedData.egitmen_adi || "Bilinmiyor";
        document.getElementById("displayEgitimSuresi").textContent = savedData.egitim_suresi || "Bilinmiyor";
        document.getElementById("displayEgitimOzeti").textContent = savedData.egitim_ozeti || "Bilinmiyor";
        document.getElementById("displayHedefKitle").textContent = savedData.hedef_kitle || "Bilinmiyor";
        document.getElementById("displayKaynakDokumanlar").textContent = savedData.kaynak_dokumanlar || "Bilinmiyor";
    }
});

// ✅ Eksik verileri kaydetme fonksiyonu
function submitForm() {
    console.log("📌 submitForm() çağırıldı.");

    let formData = {
        egitim_adi: document.getElementById("egitimAdi").value,
        egitmen_adi: document.getElementById("egitmenAdi").value,
        egitim_suresi: document.getElementById("egitimSuresi").value,
        egitim_ozeti: document.getElementById("egitimOzeti").value,
        hedef_kitle: document.getElementById("hedefKitle").value,
        kaynak_dokumanlar: document.getElementById("kaynakDokumanlar").value
    };

    // JSON verisini localStorage’a kaydet
    localStorage.setItem("egitimData", JSON.stringify(formData));

    console.log("✅ Veriler kaydedildi, yönlendirme yapılıyor...");
    window.location.href = "egitim_cikti.html";
}

async function downloadPDF() {
    try {
        console.log("📥 SelectPDF ile PDF oluşturma işlemi başlatıldı...");

        let savedData = JSON.parse(localStorage.getItem("egitimData") || "{}");

        let response = await fetch("http://127.0.0.1:8001/pdf/generate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(savedData)
        });

        if (!response.ok) {
            throw new Error(`PDF oluşturma başarısız! HTTP Hata Kodu: ${response.status}`);
        }

        let result = await response.json();
        console.log("✅ PDF başarıyla oluşturuldu:", result);

        if (result.pdf_url) {
            // PDF dosyasını indir
            window.location.href = result.pdf_url;
        } else {
            alert("PDF oluşturma başarısız!");
        }

    } catch (error) {
        console.error("PDF indirme hatası:", error);
        alert("PDF oluşturma sırasında bir hata oluştu.");
    }
}



