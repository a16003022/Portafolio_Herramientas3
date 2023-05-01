def run():
    import streamlit as st
    import pandas as pd
    import streamlit.components.v1 as components
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    from sklearn.neighbors import KNeighborsClassifier

    hide_streamlit_style = """
        <style>
        #MainMenu {visibility:hidden;}
        footer {visibility:hidden;}
        </style>
        """

    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.title("Entrenamiento y puntuación de modelos")
    components.html(
        """<hr style="height:3px;border:none; color:#333;background-color:#333" />""")

    # Carga de datos
    URL = 'https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv'
    names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
    dfIris = pd.read_csv(URL, names=names)
    dfIris = dfIris[dfIris["sepal-length"] != "sepal.length"]

    # Separación de datos en train y test
    x_train, x_test, y_train, y_test = train_test_split(dfIris[dfIris.columns[0:4]], dfIris[dfIris.columns[-1]],
                                                        test_size=0.2)

    # Widgets para selección de modelo
    modelos = {
        "Regresión Logística": LogisticRegression(max_iter=1000),
        "K-Vecinos más cercanos": KNeighborsClassifier()
    }
    modelo_seleccionado = st.selectbox("Selecciona el modelo a entrenar:", list(modelos.keys()))

    # Entrenamiento del modelo seleccionado
    modelo = modelos[modelo_seleccionado]
    score = 1.0
    # Para asegurarnos de no puntuar un modelo que se aprendió de memoria los datos
    while score == 1.0:
        modelo.fit(x_train, y_train)
        score = modelo.score(x_test, y_test)

    # Resultados del modelo
    st.write(f"El modelo {modelo_seleccionado} obtuvo una precisión de {score}")