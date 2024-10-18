import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("Meu primeiro dashboard")

abas = st.tabs(["Botao", "Radio", "Dataframe", "Grafico"])

with abas[0]:
    if st.button("Clique aqui"):
        st.text("Voce apertou o botao")

with abas[1]:
    opcao = st.radio(
    "Escolha a opcao:",
    ("Flamengo", "Corinthians", "Plameiras")
    )

    if opcao == "Flamengo":
        st.info("Vc é um urubu!")
    elif opcao == "Corinthians":
        st.warning("Vc é um campeao!")
    else:
        st.error("Voce é um perdedor")

with abas[2]:
    caminho = "C:\\Users\\21701079836\\Documents\\projetos\\frontend\\data"
    df = pd.read_csv(caminho + "\\ibov.csv")
    st.dataframe(df)


with abas[3]:
    plt.style.use('_mpl-gallery')
    # make data:
    x = 0.5 + np.arange(8)
    y = [4.8, 5.5, 3.5, 4.6, 6.5, 6.6, 2.6, 3.0]
    # plot
    fig, ax = plt.subplots()
    ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
        ylim=(0, 8), yticks=np.arange(1, 8))
    # st.pyplot(fig)
    st.pyplot(fig)














