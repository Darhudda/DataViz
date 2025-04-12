import streamlit as st
import folium
from streamlit_folium import st_folium

import pandas as pd

# Cargar el dataset
df = pd.read_csv("energia_solar.csv")

st.set_page_config(page_title="Mapa", layout="wide")

st.title("Mapa Interactivo con Folium")

m = folium.Map(location=[4.6097, -74.0818], zoom_start=6)

for i, row in df.iterrows():
    folium.Marker(
        location=[row["Latitud"], row["Longitud"]],
        popup=f"{row['Departamento']}, {row['Panel_ID']}",
        tooltip=f"Producción: {row['Producción_kWh']} kWh"
    ).add_to(m)


st_folium(m, width=700, height=500)