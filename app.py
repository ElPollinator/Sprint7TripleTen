import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Panel de autos')

df = pd.read_csv('vehicles_us.csv')

if st.button('Mostrar histograma'):
    fig = px.histogram(df, x='odometer')
    st.plotly_chart(fig)
