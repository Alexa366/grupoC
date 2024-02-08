import streamlit as st
import pandas as pd
import plotly.express as px
from proyecto1.buscador import buscador

def proyecto():

    st.title("PROYECTO 1: ESTUDIO DE PRODUCTOS DE ALIMENTACION")
    st.markdown(
        '<div style="text-align: justify;">Cuando nos planteamos este proyecto, al ver que contaban con más de 3 millones de productos, decidimos que había que acotar la selección de datos (además el notebook decía basta 💀). Finalmente cogimos 50.000 datos</p></div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify;">Donde utilizamos más tiempo en este caso fue en el Procesamiento de los Datos. Datos en forma de diccionarios, desagrupar columnas (de 50.000 pasamos a 5.433.663), hacer limpieza de datos...</p><p> Open Food Facts es una asociación sin ánimo de lucro formada por voluntarios, por lo que cada aportacion a la base de datos no tiene un patron establecido.</p></div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify;">Una vez que realizado el preprocesamiento, pudimos comenzar a realizar las visualizaciones</p></div>',
        unsafe_allow_html=True)

    df = pd.read_pickle('proyecto1/datos_spain.pkl')


    tab1, tab2, tab3 = st.tabs(["TIENDAS SEGUN ECOSCORE", "COMPARACION PRODUCTOS", "LOCALIZADOR DE TIENDAS"])

    # TIENDAS SEGUN ECOSCORE
    tab1.header("REVISION ECOSCORE")

    tab1.markdown('<div style="text-align: justify;">Gráfico con la media de datos de Ecoscore por tiendas referentes en España </p><p> Ecoscore analiza el impacto ambiental de las tiendas, donde  a mayor puntuación, menor impacto ambiental.</p></div>',
        unsafe_allow_html=True)

    tiendas = df[df['Tiendas'] != ""]['Tiendas'].dropna().value_counts().head(20).index.to_list()

    tiendas_selecc = tab1.multiselect(label = "**Elige las tiendas a comparar**",
                                      options=tiendas,default=tiendas[:4])

    df_filtrado_tiendas = df[df['Tiendas'].isin(tiendas_selecc)]

    # sacamos la media necesaria para gráficar
    df_media = df_filtrado_tiendas.groupby('Tiendas')['Puntuación Ecoscore'].mean().reset_index()
    df_media = df_media.sort_values(by='Puntuación Ecoscore', ascending=False)

    # gráficamos un tipo barplot
    fig = px.bar(df_media, x='Tiendas', y='Puntuación Ecoscore',color_discrete_sequence=['orange'])

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

    tab2.plotly_chart(figure_or_data=fig)


    tab3.write("BUSCADOR DE TIENDAS")



if __name__ == "__main__":
    proyecto()

