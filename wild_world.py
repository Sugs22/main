import streamlit as st
import pandas as pd

url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/country_data/Spain.csv'

st.write("Import data vaccination")

df = pd.read_csv(url,error_bad_lines = False)

st.write(df.head(5))
