from cgitb import reset
from itertools import count
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
    st.title('Café')

    st.write('Ganho anual dos paises exportadores')

    # exports_crop = datasets['exports-crop-year']
    exports_calendar = load_data('exports-calendar-year')
    prices_paid = load_data('prices-paid-to-growers')
    
    # st.write('exports-crop-year')
    # st.write(exports_crop)
    st.write('exports-calendar-year')
    st.write(exports_calendar)
    st.write('prices-paid-to-growers')
    st.write(prices_paid)
    
    anual_gain = pd.DataFrame()
    anual_gain['paises'] = prices_paid['prices_paid_to_growers']

    st.write('Ganho anual')
    for y in range(1990, 2019):
        year = str(y)
        anual_gain[year] = (prices_paid[year].astype(float) * 60) * exports_calendar[year].astype(float)
    st.write(anual_gain)