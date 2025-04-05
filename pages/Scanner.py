import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Scanner", layout="centered")

st.markdown("## 📷 Escaneie o código (QR ou Barras)")

components.html(
    """
    <script src="https://unpkg.com/html5-qrcode"></script>
    <div id="reader" style="width: 100%; max-width: 400px;"></div>
    <script>
        const config = {
            fps: 10,
            qrbox: 250,
            formatsToSupport: [
                Html5QrcodeSupportedFormats.QR_CODE,
                Html5QrcodeSupportedFormats.EAN_13,
                Html5QrcodeSupportedFormats.CODE_128
            ]
        };

        const scanner = new Html5Qrcode("reader");

        Html5Qrcode.getCameras().then(devices => {
            const backCam = devices.find(d => d.label.toLowerCase().includes("back")) || devices[0];
            scanner.start(
                { deviceId: { exact: backCam.id } },
                config,
                function(decodedText) {
                    window.top.location.href = window.origin + "/?ticket=" + encodeURIComponent(decodedText);
                },
                function(error) {}
            ).catch(err => {
                document.getElementById("reader").innerHTML = "🚫 Erro ao acessar a câmera.";
            });
        });
    </script>
    """,
    height=480
)
