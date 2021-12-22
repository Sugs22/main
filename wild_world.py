import streamlit as st
import pandas as pd

url = 'https://github.com/owid/covid-19-data/blob/master/public/data/vaccinations/country_data/Spain.csv'

st.write("Import data vaccination")

df = pd.read_csv(url)

st.write(df.head(5))
