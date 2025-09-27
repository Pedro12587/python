import pandas as pd
import matplotlib.pyplot as plt

# pip install stremlit

import streamlit as st

st.title("Visualização dos Dados")

# upload do Arquivo CSV

arquivo = st.file_uploader("Envie seu arquivo CSV", type=["csv"])

# verificar se o arquivo existe
if arquivo is not None:
    # ler o arquivo
    df = pd.read_csv(arquivo)

    st.write("Dados carregados:")
    st.dataframe(df)

    # selectbox - para tipo de grafico
    opcao = st.selectbox(
        "Escolha o tipo de gráfico:",
        ["Barras", "Pizza", "Linha"]
    )

    # grafico de barras
    if opcao == "Barras":
        st.bar_chart(df.set_index("nome")["quantidade"])

    # grafico de linhas
    elif opcao == "Linha":
        st.line_chart(df.set_index("nome")["quantidade"])

    # grafico de pizza
    elif opcao == "Pizza":
        st.pyplot(df.set_index("nome").plot.pie(y="quantidade").figure)

else:
    st.info("Envie um arquivo CSV com as colunas Nome e Quantidade")

# python -m streamlit run graficos_steam.py

