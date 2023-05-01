import streamlit as st
import os

# Obtener todos los archivos dentro de la carpeta "Pages" que terminen en .py
pages = [f[:-3] for f in os.listdir("Pages") if f.endswith(".py")]

# Crear una lista con el nombre de cada página
page_names = [page.split(".")[0] for page in pages]

# Mostrar una lista de páginas en el sidebar
selected_page = st.sidebar.selectbox("Selecciona una página", page_names)

# Importar y mostrar la página seleccionada
page_path = os.path.join("Pages", f"{selected_page}.py")
page_module = __import__(f"Pages.{selected_page}")
page_module.run()
