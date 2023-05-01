import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit.components.v1 as components
import numpy as np
import plotly.graph_objects as go

hide_streamlit_style= """
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.title("Visualización")
components.html(
    """<hr style="height:3px;border:none; color:#333;background-color:#333" />""")

URL= 'https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv'
dfIris= pd.read_csv(URL)

fig = px.box(dfIris, y="variety")
#dfIris.plot(kind='box', )
st.plotly_chart(fig, use_container_width=True)


st.subheader("Histogramas")
for i in range(0, len(dfIris.columns)):
    fig = px.histogram(dfIris, x=dfIris.columns[i])
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Gráfica de correlación")
fig = px.scatter_matrix(dfIris,
dimensions=dfIris.columns[0:4],
color="variety")

st.plotly_chart(fig, use_container_width=True)

st.subheader("Correlación-Mapa de color")
df_corr=dfIris.corr()
fig = go.Figure()
fig.add_trace(
    go.Heatmap(
    x= df_corr.columns,
    y= df_corr.index,
    z= np.array(df_corr)
    )
)

st.plotly_chart(fig, use_container_width=True)