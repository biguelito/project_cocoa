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


def refactor_null_processing_values(coffe_reviews):
    mask = coffe_reviews['Processing.Method'].isna()
    coffe_reviews.loc[mask, 'Processing.Method'] = coffe_reviews.loc[mask,'Processing.Method'].fillna('Washed / Wet')

def refactor_null_color_values(coffe_reviews):
    mask = coffe_reviews['Color'].isna()
    coffe_reviews.loc[mask, 'Color'] = coffe_reviews.loc[mask,'Color'].fillna('Green')

def refactor_null_variety_values(coffe_reviews):
    mask = coffe_reviews['Variety'].isna()
    coffe_reviews.loc[mask, 'Variety'] = coffe_reviews.loc[mask,'Variety'].fillna('Caturra')

if __name__ == '__main__':
    datasets = {}
    listagem_datasets = os.listdir('.\\dataset\\')
    for dataset in listagem_datasets:
        dt = dataset.split('.')[0]
        datasets[dt] = load_data(dt)
    
    st.title('Café')

    # datasets_state = st.text('Carregando datasets')
    # for dataset_nome, dataset in datasets.items():
    #     st.text(dataset_nome)
    #     st.write(dataset)
    # datasets_state.text("Dados do café")

    st.markdown("# Dataset de Reviews")

    merged_coffe_reviews = pd.read_csv('dataset\\merged_data_cleaned.csv')

    st.markdown("""#### Exibiremos os primeiros e os últimos cinco registros para entendermos melhor a estrutura dos dados.""")
    st.write(merged_coffe_reviews.head())
    st.write(merged_coffe_reviews.tail())
    st.write(merged_coffe_reviews.shape)

    st.markdown("""#### Checando valores únicos.""")
    st.write(merged_coffe_reviews.nunique(dropna=False))

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
    st.write(coffe_reviews.nunique(dropna=False))

    st.markdown("""#### Checando os valores nulos.""")
    st.write(coffe_reviews.isnull().sum())

    st.markdown("""#### Análise dos Dados""")
    country_entries = coffe_reviews['Country.of.Origin'].value_counts().to_frame()
    country_entries = country_entries.reset_index()
    country_entries.columns = ['Países', 'Registros']
    st.write(country_entries)

    st.markdown("""#### Gráfico de barra País/Registros""")
    chart = alt.Chart(country_entries).mark_bar().encode(
        x = 'Registros',
        y = alt.Y('Países', sort='-x'),
        tooltip=['Registros']
    )
    st.altair_chart(chart, use_container_width=True)

    st.markdown('### Capturando Outliers')
    st.markdown('#### Método de processamentos')
    processing_method = coffe_reviews['Processing.Method'].value_counts(dropna=False)
    st.write(processing_method)

    st.markdown('#### Cor dos grãos')
    coffe_reviews.loc[coffe_reviews.Color == 'Blue-Green', 'Color'] = 'Bluish-Green'
    color_of_coffee = coffe_reviews['Color'].value_counts(dropna=False)
    st.write(color_of_coffee)

    st.markdown('#### Variedade dos Grãos')
    variety_of_coffee = coffe_reviews['Variety'].value_counts(dropna=False)
    st.write(variety_of_coffee)

    outliers_processing = coffe_reviews[coffe_reviews['Processing.Method'].isna()]
    outliers_color = coffe_reviews[coffe_reviews['Color'].isna()]
    outliers_variety = coffe_reviews[coffe_reviews['Variety'].isna()]
    outliers = coffe_reviews[coffe_reviews['Processing.Method'].isna()| coffe_reviews['Color'].isna()|coffe_reviews['Variety'].isna()]

    st.markdown('#### Outliers Processing')
    st.write(outliers_processing)
    st.write(outliers_processing.shape)
    st.markdown('#### Método de processamentos sem nulos')
    refactor_null_processing_values(coffe_reviews)
    #Inclusão do código visualmente no streamlit --------------------------------------------
    st.code("""
    mask = coffe_reviews['Processing.Method'].isna()
    coffe_reviews.loc[mask, 'Processing.Method'] = coffe_reviews.loc[mask,'Processing.Method'].fillna('Washed / Wet')
    """)
    #----------------------------------------------------------------------------------------
    st.write(coffe_reviews)
    st.write(coffe_reviews['Processing.Method'].value_counts(dropna=False))

    st.markdown('#### Outliers Colors')
    st.write(outliers_color)
    st.write(outliers_color.shape)
    st.markdown('#### Cor dos grãos sem nulos')
    refactor_null_color_values(coffe_reviews)
    st.code("""
    mask = coffe_reviews['Color'].isna()
    coffe_reviews.loc[mask, 'Color'] = coffe_reviews.loc[mask,'Color'].fillna('Green')
    """)
    st.write(coffe_reviews)
    st.write(coffe_reviews['Color'].value_counts(dropna=False))

    st.markdown('#### Outliers Variety')
    st.write(outliers_variety)
    st.write(outliers_variety.shape)
    st.markdown('#### Variedade dos Grãos sem nulos')
    refactor_null_variety_values(coffe_reviews)
    st.code("""
    mask = coffe_reviews['Variety'].isna()
    coffe_reviews.loc[mask, 'Variety'] = coffe_reviews.loc[mask,'Variety'].fillna('Caturra')
    """)
    st.write(coffe_reviews)
    st.write(coffe_reviews['Variety'].value_counts(dropna=False))

    st.markdown('#### Outliers')
    st.write(outliers)
    st.write(outliers.shape)