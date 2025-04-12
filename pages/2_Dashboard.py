import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard", layout="wide")
st.title(" Dashboard de Datos")

data = pd.DataFrame({
    "Categoría": ["A", "B", "C", "D"],
    "Valores": [23, 17, 35, 29]
})

st.dataframe(data)

fig, ax = plt.subplots()
ax.bar(data["Categoría"], data["Valores"], width=0.4)
st.pyplot(fig)

