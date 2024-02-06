import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from proyecto1.buscador import buscador

def proyecto():

    st.title("ESTUDIO DE PRODUCTOS DE ALIMENTACION")

    tab1, tab2, tab3 = st.tabs(["TIENDAS SEGUN ECOSCORE", "COMPARACION PRODUCTOS", "LOCALIZADOR DE TIENDAS"])

    tab1.write("REVISION ECOSCORE")

    df = pd.read_pickle('proyecto1/datos_spain.pkl')

    tab1.header('Tiendas')
    tiendas = df[df['Tiendas'] != ""]['Tiendas'].dropna().value_counts().head(20).index.to_list()

    tiendas_selecc = tab1.multiselect(label = "**Elige las tiendas a comparar**",
                                      options=tiendas,default=tiendas[:4])

    df_filtrado_tiendas = df[df['Tiendas'].isin(tiendas_selecc)]

    # sacamos la media necesaria para gráficar
    df_media = df_filtrado_tiendas.groupby('Tiendas')['Puntuación Ecoscore'].mean().reset_index()
    df_media = df_media.sort_values(by='Puntuación Ecoscore', ascending=False)

    # gráficamos un tipo barplot
    fig = px.bar(df_media, x='Tiendas', y='Puntuación Ecoscore')

    fig.update_layout(
        title="Media de Puntuación Ecoscore en Tiendas",
        xaxis_title="Tiendas",
        yaxis_title="Media de Puntuación Ecoscore")

    tab1.plotly_chart(figure_or_data=fig)

    tab2.write("COMPARACION PRODUCTOS")

    marcas = df['Marcas'].dropna().unique()
    marca = tab2.multiselect("MARCAS", marcas, ['Nocilla', 'Nutella'])

    datos = tab2.radio("Elige", ["Grasas", "kcal", "Grasas saturadas", "Azucares"], horizontal=True)

    df_filtrado_marcas = df[df["Marcas"].isin(marca)]
    agrupado = df_filtrado_marcas.groupby("Marcas")[["Grasas", "kcal", "Grasas saturadas", "Azucares"]].mean()

    fig = px.bar(data_frame=agrupado[datos],
                 x=marca,
                 y=datos)

    tab2.plotly_chart(figure_or_data=fig))


    tab3.write("BUSCADOR DE TIENDAS")
    buscador()


if __name__ == "__main__":
    proyecto()

