import streamlit as st
from extractor import extrair_ips

st.set_page_config(
    page_title="Leitor de Bilhetes",
    page_icon="🌐",
    layout="wide"
)

st.title("🌐 Leitor de Bilhetes")

st.write(
    "Cole o texto do bilhete abaixo e clique em 'Analisar'."
)

texto = st.text_area(
    "Bilhete",
    height=300
)

if st.button("Analisar"):

    if not texto.strip():
        st.warning("Insira um bilhete.")
    else:

        resultado = extrair_ips(texto)

        st.subheader("IPs encontrados")

        encontrou = False

        for tipo, info in resultado.items():

            if info["ip"]:

                encontrou = True

                st.success(
                    f"{tipo}: {info['ip']} {info['barramento'] or ''}"
                )

        if not encontrou:
            st.error("Nenhum IP encontrado.")