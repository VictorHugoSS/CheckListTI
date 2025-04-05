import streamlit as st
from datetime import date

st.set_page_config(page_title="Checklist", layout="centered")

# Recuperar ticket da URL (caso venha do scanner)
ticket_param = st.query_params.get("ticket", "")

st.title("📋 Checklist com Scanner Externo")

# Campo preenchido via URL
ticket = st.text_input("Número do Ticket", value=ticket_param)

# Botão que leva para a página do scanner
st.markdown("[📷 Escanear Código](/Scanner)", unsafe_allow_html=True)

# Demais campos
colaborador = st.text_input("Colaborador")
data = st.date_input("Data", value=date.today())

st.markdown("### Itens de Verificação")
col1, col2 = st.columns(2)
with col1:
    check1 = st.checkbox("Equipamento limpo")
    check2 = st.checkbox("Sem vazamentos")
    check3 = st.checkbox("Sinalização adequada")
with col2:
    check4 = st.checkbox("EPI utilizado corretamente")
    check5 = st.checkbox("Área isolada")

observacoes = st.text_area("Observações")

if st.button("Salvar"):
    dados = {
        "ticket": ticket,
        "colaborador": colaborador,
        "data": data.isoformat(),
        "equipamento_limpo": check1,
        "sem_vazamentos": check2,
        "sinalizacao": check3,
        "uso_epi": check4,
        "area_isolada": check5,
        "observacoes": observacoes
    }
    st.success("Checklist salvo com sucesso!")
    st.write(dados)
