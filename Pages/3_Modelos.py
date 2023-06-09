def run():
    import pandas as pd
    import streamlit as st
    import streamlit.components.v1 as components
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import StratifiedKFold
    from sklearn.model_selection import cross_val_score
    from sklearn.neighbors import KNeighborsClassifier

    hide_streamlit_style = """
        <style>
        #MainMenu {visibility:hidden;}
        footer {visibility:hidden;}
        </style>
        """

    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.title("Entreamiento y precisión de modelos")
    components.html(
        """<hr style="height:3px;border:none; color:#333;background-color:#333" />""")

    URL = 'https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv'
    names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
    dfIris = pd.read_csv(URL, names=names)
    dfIris = dfIris[dfIris["sepal-length"] != "sepal.length"]

    x_train, x_test, y_train, y_test = train_test_split(dfIris[dfIris.columns[0:4]], dfIris[dfIris.columns[-1]],
                                                        test_size=0.2)

    modelos = []
    # print(x_train, x_test)
    modelo = LogisticRegression(random_state=0).fit(x_train, y_train)
    modelo.score(x_test, y_test)
    modelo.predict(x_test)
    modelos.append(("LR", LogisticRegression()))

    st.subheader("Modelo Regresión Lineal")
    st.write("Puntuación:")
    st.write(modelo.score(x_test, y_test))
    st.write("Resultados de predicciones:")
    st.write(modelo.predict(x_test))

    st.subheader("Modelo KFold")
    skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=1)
    model = KNeighborsClassifier(n_neighbors=3)
    scores = []
    predictions = []
    for train_index, test_index in skf.split(x_train, y_train):
        x_train_fold, x_test_fold = x_train.iloc[train_index], x_train.iloc[test_index]
        y_train_fold, y_test_fold = y_train.iloc[train_index], y_train.iloc[test_index]
        model.fit(x_train_fold, y_train_fold)
        scores.append(model.score(x_test_fold, y_test_fold))
        predictions.append(model.predict(x_test))
    average_score = sum(scores) / len(scores)
    st.write("Precisión del modelo:")
    st.write(average_score)
    st.write("Resultados de predicciones:")
    for i, pred in enumerate(predictions):
        st.write(f"Fold {i + 1}: {pred}")

    st.subheader("Modelo KNeigghbors")
    modeloKN = KNeighborsClassifier(n_neighbors=3)
    modeloKN.fit(x_train, y_train)
    st.write("Precisión del modelo")
    st.write(modeloKN.score(x_test, y_test))
    st.write("Resultados de predicciones:")
    st.write(modeloKN.predict(x_test))
