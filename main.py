import streamlit as st
import os

# Obtener todas las páginas .py en la carpeta Pages
pages = [f[:-3] for f in os.listdir("Pages") if f.endswith(".py")]

# Agregar la página seleccionada a la barra lateral
selection = st.sidebar.selectbox("Ir a", pages)

# Importar la página seleccionada y ejecutarla
page = __import__(f"Pages.{selection}")
page.run()

