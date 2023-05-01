import streamlit as st
import os

# Obtener todos los archivos dentro de la carpeta "Pages"
pages = os.listdir("Pages")

# Mostrar un slidebar con todos los archivos
selected_page = st.sidebar.selectbox("Selecciona una página", pages)

# Cargar la página seleccionada
page_path = os.path.join("Pages", selected_page)
with open(page_path, "r") as f:
    st.markdown(f.read())