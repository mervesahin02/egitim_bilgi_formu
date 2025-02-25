document.addEventListener("DOMContentLoaded", function () {

    // 📌 Dosya yükleme sayfası
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
                    localStorage.setItem("egitimData", JSON.stringify(result.parsed_data));
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

    // 📌 Eksik veri formu sayfası
    if (document.getElementById("missingDataForm")) {
        let savedData = JSON.parse(localStorage.getItem("egitimData") || "{}");

        document.getElementById("id").value = savedData.id || "";
        document.getElementById("egitimAdi").value = savedData.egitim_adi || "";
        document.getElementById("egitmenAdi").value = savedData.egitmen_adi || "";
        document.getElementById("egitimSuresi").value = savedData.egitim_suresi || "";
        document.getElementById("egitimOzeti").value = savedData.egitim_ozeti || "";
        document.getElementById("hedefKitle").value = savedData.hedef_kitle || "";
        document.getElementById("kaynakDokumanlar").value = savedData.kaynak_dokumanlar || "";

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

        // Yazdırma sırasında butonları gizle
        window.onbeforeprint = function () {
            document.getElementById("printBtn").style.display = "none";
            document.getElementById("wordDownloadBtn").style.display = "none";
        };

        window.onafterprint = function () {
            document.getElementById("printBtn").style.display = "block";
            document.getElementById("wordDownloadBtn").style.display = "block";
        };
    }
});

// ✅ Eksik verileri kaydetme fonksiyonu
function submitForm() {
    let formData = {
        id: document.getElementById("id").value,
        egitim_adi: document.getElementById("egitimAdi").value,
        egitmen_adi: document.getElementById("egitmenAdi").value,
        egitim_suresi: document.getElementById("egitimSuresi").value,
        egitim_ozeti: document.getElementById("egitimOzeti").value,
        hedef_kitle: document.getElementById("hedefKitle").value,
        kaynak_dokumanlar: document.getElementById("kaynakDokumanlar").value
    };

    localStorage.setItem("egitimData", JSON.stringify(formData));
    window.location.href = "egitim_cikti.html";
}

// ✅ Yazdırma işlemi
function printPage() {
    window.print();
}

// ✅ Word dosyası dönüştürme işlemi (masaüstünden dosya seçilecek)
function convertToWord() {
    let fileInput = document.createElement("input");
    fileInput.type = "file";
    fileInput.accept = ".pdf";
    fileInput.style.display = "none";

    fileInput.addEventListener("change", function () {
        let file = fileInput.files[0];

        if (file) {
            let formData = new FormData();
            formData.append("pdf_path", file);

            fetch("http://127.0.0.1:8001/word/generate", {
                method: "POST",
                body: formData
            })
                .then(response => response.blob())
                .then(blob => {
                    let link = document.createElement("a");
                    link.href = URL.createObjectURL(blob);
                    link.download = "egitim_bilgileri.docx";
                    link.click();
                })
                .catch(error => console.error("Hata:", error));
        }
    });

    fileInput.click();
}
document.addEventListener("DOMContentLoaded", function () {

    // 📌 Çıktı sayfasında mıyız?
    if (document.getElementById("outputContainer")) {
        let savedData = JSON.parse(localStorage.getItem("egitimData") || "{}");

        document.getElementById("displayEgitimAdi").textContent = savedData.egitim_adi || "Bilinmiyor";
        document.getElementById("displayEgitmenAdi").textContent = savedData.egitmen_adi || "Bilinmiyor";
        document.getElementById("displayEgitimSuresi").textContent = savedData.egitim_suresi || "Bilinmiyor";
        document.getElementById("displayEgitimOzeti").textContent = savedData.egitim_ozeti || "Bilinmiyor";
        document.getElementById("displayHedefKitle").textContent = savedData.hedef_kitle || "Bilinmiyor";
        document.getElementById("displayKaynakDokumanlar").textContent = savedData.kaynak_dokumanlar || "Bilinmiyor";
        document.getElementById("displayEgitimID").textContent = savedData.id || "Bilinmiyor";

        // 📌 Yazdırma sırasında butonları gizle
        window.onbeforeprint = function () {
            document.getElementById("printBtn").style.display = "none";
            document.getElementById("wordConvertBtn").style.display = "none";
        };

        window.onafterprint = function () {
            document.getElementById("printBtn").style.display = "block";
            document.getElementById("wordConvertBtn").style.display = "block";
        };
    }
});

// ✅ Sayfayı yazdır
function printPage() {
    window.print();
}

// ✅ PDF seçme ekranını göster
function showPdfUpload() {
    document.getElementById("pdfUploadContainer").style.display = "block";
}

// ✅ PDF'den Word'e çevir
function convertToWord() {
    let fileInput = document.getElementById("pdfFileInput").files[0];

    if (!fileInput) {
        alert("Lütfen bir PDF dosyası seçin!");
        return;
    }

    let formData = new FormData();
    formData.append("file", fileInput);

    fetch("http://127.0.0.1:8001/word/convert", {
        method: "POST",
        body: formData
    })
        .then(response => response.blob())
        .then(blob => {
            let link = document.createElement("a");
            link.href = URL.createObjectURL(blob);
            link.download = "egitim_bilgileri.docx";
            link.click();
        })
        .catch(error => console.error("Hata:", error));
}
