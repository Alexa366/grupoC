import streamlit as st
import numpy as np
import pickle
import pandas as pd
from proyecto2.ml import modelo_filtrado


def proyecto2es():
    st.title("PROYECTO 2: CREACION DE UN MODELO DE MACHINE LEARNING PARA DETECTAR SI UNA SETA ES VENENOSA O COMESTIBLE")
    st.markdown(
        '<div style="text-align: justify;">Basandonos en el DataFrame de UCI Machine Learning Repository, empezamos a realizar nuestro segundo proyecto</p></div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify;">Tras un estudio de cualés eran las partes y características que componen una seta, y la información encontrada en el Dataset, realizamos el EDA y el preprocesado de los datos. Dividimos el análisis de los datos por las partes que componen la seta, para una mejor explicación de los mismos.</p></div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify;">En el EDA nos dimos cuenta que algunas características tenían un gran peso a la hora de predecir el resultado, que se refrendó al probar los diferenctes modelos de clasificación de Machine Learning, donde la mayoría de los modelo daban un 100% de Accuracy, Precision y Recall</p></div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify;">Eso nos hice revisar el proyecto para darle un poco más de valor al mismo, y decidimos comprobar para cada tipo de característica cual sería la precisión del mismo. Para realizar la predicción nos quedamos con el modelo de RandomForest. Os animamos a que elijáis entre las diferentes opciones para la comprobacion de si una 🍄 es comestible o venenosa</p></div>',
        unsafe_allow_html=True)

    st.subheader("MODELO DE ML: SETAS, ¿COMESTIBLES O VENENOSAS?")

    df = pd.read_csv("proyecto2/setas.csv").drop('class', axis=1)
    df2 = pd.read_csv("proyecto2/setas.csv")

    with st.expander(label="DataFrame", expanded=False):
        st.dataframe(df2)

    sombrero = [x for x in df.columns if 'sombrero' in x]

    lamina = [x for x in df.columns if 'lamina' in x]

    tallo = [x for x in df.columns if 'tallo' in x]

    resto = [x for x in df.columns if not any(y in x for y in ('sombrero', 'lamina', 'tallo'))]

    datos = []
    seleccion = []

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header('Sombrero')
        # Sombrero
        for column in df[sombrero].columns.to_list():
            dato_sombrero = ["All"] + list(df[column].unique())
            sombreros = st.selectbox(label= f"{column}",
                             options=dato_sombrero,
                             index=0)
            datos.append(f"{column}" if sombreros != "All" else None)
            if sombreros !='All':
                seleccion.append(sombreros)

    with col2:
        st.header('Laminas')
        # Laminas
        for column in df[lamina].columns.to_list():
            dato_laminas = ["All"] + list(df[column].unique())
            laminas = st.selectbox(label=f"{column}",
                         options=dato_laminas,
                         index=0)
            datos.append(f"{column}" if laminas != "All" else None)
            if laminas !='All':
                seleccion.append(laminas)

    with col3:
        st.header('Tallo')
        # Tallo
        for column in df[tallo].columns.to_list():
            dato_tallo = ["All"] + list(df[column].unique())
            tallos = st.selectbox(label=f"{column}",
                         options=dato_tallo,
                         index=0)
            datos.append(f"{column}" if tallos != "All" else None)
            if tallos !='All':
                seleccion.append(tallos)

    with col1:
        st.header('Otras Caract.')
        for column in df[resto[:3]].columns.to_list():
            dato_otros = ["All"] + list(df[column].unique())
            otros_1 = st.selectbox(label=f"{column}",
                         options=dato_otros,
                         index=0)
            datos.append(f"{column}" if otros_1 != "All" else None)
            if otros_1 !='All':
                seleccion.append(otros_1)

    with col2:
        st.header('Otros')
        for column in df[resto[4:]].columns.to_list():
            dato_otros = ["All"] + list(df[column].unique())
            otros_2 = st.selectbox(label=f"{column}",
                         options=dato_otros,
                         index=0)
            datos.append(f"{column}" if otros_2 != "All" else None)
            if otros_2 !='All':
                seleccion.append(otros_2)

    prediccion = tuple([x for x in datos if not x == None])
    prediccion_list = [x for x in datos if not x == None]
    with open('proyecto2/dicc.pkl', 'rb') as file:
        diccionario = pickle.load(file)

    col3.header('Prediccion')
    if prediccion == ():
        col3.write("Elige una opcion")
    else:
        test = []
        for datos, valor in zip(prediccion, seleccion):
            test.append(diccionario[datos][valor])

        test = np.array([test])

        test = modelo_filtrado(prediccion)[1].transform(test)
        model = modelo_filtrado(prediccion)[0]
        y_pred = model.predict(test)
        for k, v in diccionario['class'].items():
            if v == y_pred[0]:
                resultado = k

        if resultado == 'comestible':
            col3.metric("PREDICTION", f'{resultado}'.upper())
        else:
            col3.metric("PREDICTION", f'{resultado}'.upper())

        col3.metric("ACCURACY", modelo_filtrado(prediccion)[2])
        col3.metric("PRECISSION", modelo_filtrado(prediccion)[3])
        col3.metric("RECALL", modelo_filtrado(prediccion)[4])

if __name__ == "__main__":
    proyecto2es()