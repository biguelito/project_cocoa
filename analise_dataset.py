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
    data_load_state.text("Done! (using st.cache)")

    st.subheader('Raw data')
    st.write(cocoa)