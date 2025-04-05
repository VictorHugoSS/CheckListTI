import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Scanner", layout="centered")

st.markdown("## 📷 Escaneie o código")

# Scanner com redirecionamento após leitura
components.html(
    """
    <script src="https://unpkg.com/html5-qrcode"></script>
    <div id="reader" style="width: 100%; max-width: 400px;"></div>
    <script>
        const scanner = new Html5Qrcode("reader");
        scanner.start(
            { facingMode: { exact: "environment" } },
            { fps: 10, qrbox: 250 },
            function(decodedText) {
                window.location.href = "/?ticket=" + encodeURIComponent(decodedText);
            },
            function(error) {}
        ).catch(err => {
            document.getElementById("reader").innerHTML = "🚫 Erro ao abrir câmera.";
        });
    </script>
    """,
    height=460
)
