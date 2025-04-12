import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import pandas as pd

# Configuración de la app
st.set_page_config(page_title="App con Mapas", layout="wide")

# Menú lateral
with st.sidebar:
    selected = option_menu("Menú", ["Inicio", "Mapa", "Dashboard"],
        icons=["house", "geo-alt", "bar-chart"], menu_icon="cast", default_index=0)

# Página de inicio con contexto
if selected == "Inicio":
    st.title("Bienvenido a la App Interactiva 🌞")
    st.markdown(
        """
        Esta aplicación interactiva permite explorar datos de **producción solar** 
        en diferentes departamentos de **Colombia**, a través de mapas y dashboards.

        **¿Qué puedes hacer aquí...?**
        - Visualizar en un mapa la ubicación de paneles solares con su producción energética. 
        - Filtrar por departamento o características específicas.
        - Analizar patrones de producción según variables como las horas de sol.

        ---
        """
    )

    # Imagen alusiva
    imagen = Image.open("panel_solar.jpg")
    st.image(imagen, caption="Paneles solares en Colombia", use_column_width=True)
    st.caption("Imagen tomada de [Ministerio de Minas y Energía de Colombia](https://www.minenergia.gov.co/)")


    # Carga rápida del CSV y resumen
    df = pd.read_csv("energia_solar.csv")
    st.subheader("Resumen de la base de datos")
    st.dataframe(df.head())

    st.markdown(
        f"""
        - Total de registros: **{len(df)}**
        - Departamentos incluidos: **{df['Departamento'].nunique()}**
        - Producción promedio: **{round(df['Producción_kWh'].mean(), 2)} kWh**
        - Rango de horas de sol: **{df['Horas_Sol_Diarias'].min()} - {df['Horas_Sol_Diarias'].max()} horas**
        """
    )

elif selected == "Mapa":
    st.switch_page("pages/1_Mapa.py")
elif selected == "Dashboard":
    st.switch_page("pages/2_Dashboard.py")
