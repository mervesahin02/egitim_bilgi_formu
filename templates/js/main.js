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

    const downloadBtn = document.getElementById("downloadBtn");
    const pdfForm = document.getElementById("pdfForm");
    
    // Butona tıklanması durumunda formu göster
    downloadBtn.addEventListener("click", function() {
        pdfForm.style.display = "block";  // Formu göster
        downloadBtn.style.display = "none";  // Butonu gizle
    });

    // Form gönderildiğinde PDF yolunu backend'e gönder
    pdfForm.addEventListener("submit", function(event) {
        event.preventDefault();  // Sayfa yenilenmesini engelle
        
        const pdfPath = document.getElementById("pdf_path").value;
        
        if (pdfPath) {
            // PDF yolunu backend'e POST et
            fetch("http://localhost:8001/word/generate", {
                method: "POST",
                body: new URLSearchParams({
                    pdf_path: pdfPath
                }),
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded"
                }
            })
            .then(response => response.blob())
            .then(blob => {
                // Dosyayı indirmek için bir link oluştur
                const link = document.createElement("a");
                link.href = URL.createObjectURL(blob);
                link.download = "egitim_bilgileri.docx";
                link.click();
            })
            .catch(error => {
                console.error("Hata oluştu:", error);
            });
        }
    });
});

async function downloadWord() {
    try {
        console.log("📥 Word oluşturma işlemi başlatıldı...");

        let savedData = JSON.parse(localStorage.getItem("egitimData") || "{}");

        // JSON verisini düzgün formatta gönder
        let response = await fetch("http://127.0.0.1:8001/word/generate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(savedData)
        });

        if (!response.ok) {
            throw new Error(`Word oluşturma başarısız! HTTP Hata Kodu: ${response.status}`);
        }

        let result = await response.json();
        console.log("✅ Word başarıyla oluşturuldu:", result);

        if (result.file_path) {
            // Geçici dosyayı frontend templates kısmından indir
            window.location.href = "http://127.0.0.1:8001/static/" + result.file_path.split("/").pop();
        } else {
            alert("Word oluşturma başarısız!");
        }

    } catch (error) {
        console.error("Word indirme hatası:", error);
        alert("Word oluşturma sırasında bir hata oluştu.");
    }
}


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

function printPage() {
    window.print();  // 🔥 Tarayıcının yazdırma diyaloğunu açar
}

function downloadHTML() {
    const content = document.documentElement.outerHTML;  // 🔥 Sayfanın tüm HTML içeriğini al
    const blob = new Blob([content], { type: "text/html" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "egitim_cikti.html";  // 🔥 İndirilecek dosyanın ismi
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}
