import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Mapa", layout="wide")

st.title("Mapa Interactivo con Folium")

m = folium.Map(location=[4.6097, -74.0818], zoom_start=6)

folium.Marker(
    location=[4.6097, -74.0818],
    popup="Bogotá",
    tooltip="Click para más info"
).add_to(m)

st_folium(m, width=700, height=500)