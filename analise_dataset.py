from cgitb import reset
from itertools import count
import seaborn as sns
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
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
    
    st.title('Café')

    datasets_state = st.text('Carregando datasets')
    for dataset_nome, dataset in datasets.items():
        st.text(dataset_nome)
        st.write(dataset)
    datasets_state.text("Dados do café")

    st.markdown("# Dataset de Reviews")

    merged_coffe_reviews = pd.read_csv('dataset\\merged_data_cleaned.csv')

    st.markdown("""#### Exibiremos os primeiros e os últimos cinco registros para entendermos melhor a estrutura dos dados.""")
    st.write(merged_coffe_reviews.head())
    st.write(merged_coffe_reviews.tail())
    st.write(merged_coffe_reviews.shape)

    st.markdown("""#### Checando valores únicos.""")
    st.write(merged_coffe_reviews.nunique())

    st.markdown("""#### Checando os valores nulos.""")
    st.write(merged_coffe_reviews.isnull().sum())

    st.markdown("""Removeremos colunas irrelevantes para futuras análises.""")
    coffe_reviews = merged_coffe_reviews.drop(['Owner', 'Farm.Name', 'Lot.Number', 
    'Mill','ICO.Number', 'Company', 'Altitude', 'Region', 'Producer', 'In.Country.Partner', 
    'Owner.1', 'Certification.Body', 'Certification.Address', 'Certification.Contact', 
    'unit_of_measurement', 'altitude_low_meters', 'altitude_high_meters', 'Bag.Weight', 'Number.of.Bags'], axis=1)
    
    #Inclusão do código visualmente no streamlit --------------------------------------------
    st.code("""coffe_reviews = merged_coffe_reviews.drop(['Owner', 'Farm.Name', 'Lot.Number', 
    'Mill','ICO.Number', 'Company', 'Altitude', 'Region', 'Producer', 'In.Country.Partner', 
    'Owner.1', 'Certification.Body', 'Certification.Address', 'Certification.Contact', 
    'unit_of_measurement', 'altitude_low_meters', 'altitude_high_meters', 'Bag.Weight', 'Number.of.Bags'], axis=1)""")
    #----------------------------------------------------------------------------------------

    st.markdown("""#### Novamente exibiremos os primeiros e os últimos cinco registros.""")
    st.write(coffe_reviews.head())
    st.write(coffe_reviews.tail())
    st.write(coffe_reviews.shape)

    st.markdown("""#### Checando valores únicos.""")
    st.write(coffe_reviews.nunique())

    st.markdown("""#### Checando os valores nulos.""")
    st.write(coffe_reviews.isnull().sum())

    country_entries = coffe_reviews.filter(['Country.of.Origin']).value_counts()
    df_country_entries = pd.DataFrame(country_entries)
    df_country_entries = df_country_entries.reset_index()
    df_country_entries.columns = ['Country', 'Entries']

    st.write(df_country_entries)