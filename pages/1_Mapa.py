import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Mapa", layout="wide")
st.title("🗺️ Mapa Interactivo de Producción Solar")

# Cargar datos
df = pd.read_csv("energia_solar.csv")
df["Latitud"] = df["Latitud"].astype(float)
df["Longitud"] = df["Longitud"].astype(float)
df.columns = df.columns.str.strip()

# Filtro por departamento
departamentos = df["Departamento"].unique().tolist()
departamento_seleccionado = st.selectbox("Selecciona un departamento", ["Todos"] + departamentos)

# Filtrar el dataframe
if departamento_seleccionado != "Todos":
    df_filtrado = df[df["Departamento"] == departamento_seleccionado]
else:
    df_filtrado = df

# Centro del mapa calculado dinámicamente
centro_lat = df_filtrado["Latitud"].mean()
centro_lon = df_filtrado["Longitud"].mean()

# Crear mapa
m = folium.Map(location=[centro_lat, centro_lon], zoom_start=6)

# Marcadores dinámicos
if departamento_seleccionado == "Todos":
    # Agrupar por departamento
    resumen = df.groupby("Departamento").agg({
        "Latitud": "mean",
        "Longitud": "mean",
        "Producción_kWh": "mean",
        "Horas_Sol_Diarias": "mean"
    }).reset_index()

    for _, row in resumen.iterrows():
        folium.CircleMarker(
            location=[row["Latitud"], row["Longitud"]],
            radius=8,
            color="green",
            fill=True,
            fill_opacity=0.7,
            popup=(
                f"<b>{row['Departamento']}</b><br>"
                f"Prom. Producción: {round(row['Producción_kWh'], 2)} kWh<br>"
                f"Prom. Sol: {round(row['Horas_Sol_Diarias'], 2)} hrs"
            ),
            tooltip=row["Departamento"]
        ).add_to(m)
else:
    # Mostrar todos los paneles del departamento seleccionado
    for _, row in df_filtrado.iterrows():
        folium.CircleMarker(
            location=[row["Latitud"], row["Longitud"]],
            radius=6,
            color="blue",
            fill=True,
            fill_opacity=0.7,
            popup=(
                f"<b>{row['Panel_ID']}</b><br>"
                f"Producción: {row['Producción_kWh']} kWh<br>"
                f"Sol diario: {row['Horas_Sol_Diarias']} hrs"
            ),
            tooltip=row["Departamento"]
        ).add_to(m)


# Mostrar mapa
st_data = st_folium(m, width=800, height=500)

# Texto debajo del mapa (resumen del departamento)
st.markdown("---")
if departamento_seleccionado != "Todos":
    prod_prom = round(df_filtrado["Producción_kWh"].mean(), 2)
    sol_prom = round(df_filtrado["Horas_Sol_Diarias"].mean(), 2)
    num_paneles = len(df_filtrado)

    st.subheader(f"🔎 Datos generales para {departamento_seleccionado}")
    st.markdown(
        f"""
        - Número de paneles registrados: **{num_paneles}**  
        - Producción promedio: **{prod_prom} kWh**  
        - Horas de sol promedio: **{sol_prom} hrs**
        """
    )
else:
    st.info("Selecciona un departamento en el menú para ver estadísticas detalladas debajo del mapa.")