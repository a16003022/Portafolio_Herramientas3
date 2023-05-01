import streamlit as st
import os
import importlib

# Obtener todas las páginas .py en la carpeta Pages
pages = [f[:-3] for f in os.listdir("Pages") if f.endswith(".py")]

# Agregar la página seleccionada a la barra lateral
selection = st.sidebar.radio("Seleccionar página:", pages)

# Importar la página seleccionada y ejecutarla
page_module = importlib.import_module(f"Pages.{selection}")
page_module.run()

