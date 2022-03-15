from cgitb import reset
from itertools import count
import streamlit as st
import pandas as pd
import numpy as np
import os


@st.cache
def load_data(dataset, rows=100):
    data = pd.read_csv(f'dataset\\{dataset}.csv', nrows=rows)
    return data


if __name__ == '__main__':
    datasets = {}
    listagem_datasets = os.listdir('.\\dataset\\')
    for dataset in listagem_datasets:
        dt = dataset.split('.')[0]
        datasets[dt] = load_data(dt)
    
    st.title('COCOA?')

    datasets_state = st.text('Carregando datasets')
    for dataset_nome, dataset in datasets.items():
        st.text(dataset_nome)
        st.write(dataset)
    datasets_state.text("Dados do café")
    