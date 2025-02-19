const API_BASE_URL = "http://127.0.0.1:8000"; // Backend adresi

document.addEventListener("DOMContentLoaded", function () {
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
                let response = await fetch(`${API_BASE_URL}/docx/read`, {
                    method: "POST",
                    body: formData
                });

                let result = await response.json();

                if (result.parsed_data) {
                    localStorage.setItem("egitimData", JSON.stringify(result.parsed_data));
                    window.location.href = "eksik_veri_formu.html";
                }
            } catch (error) {
                console.error("Hata:", error);
                alert("Dosya yükleme başarısız!");
            }
        });
    }
});
