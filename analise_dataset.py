from cgitb import reset
from itertools import count
import streamlit as st
import pandas as pd
import numpy as np


@st.cache
def load_data(rows=2712):
    data = pd.read_csv('dataset\\chocolate_ratings.csv', nrows=rows)
    return data


if __name__ == '__main__':
    st.title('COCOA')

    data_load_state = st.text('Loading data...')
    cocoa = load_data()
    data_load_state.text("Analise de dados do dataset Cocoa")

    st.subheader('Dado integral')
    st.write(cocoa)

    st.subheader('Histograma de Quantidade/Notas')
    quantidade_por_notas = cocoa.groupby(['Rating']).size()
    st.bar_chart(quantidade_por_notas)
    st.subheader('Linha do tempo das Reviews')
    quantidade_por_data = cocoa.groupby(['Review Date']).size()
    st.area_chart(quantidade_por_data)

    st.subheader('Origem das Sementes')
    origem_sementes_qtd = cocoa.groupby(['Country of Bean Origin']).size()
    cocoa_hist = st.bar_chart(origem_sementes_qtd)