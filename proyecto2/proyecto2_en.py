import streamlit as st
import numpy as np
import pickle
import pandas as pd
from proyecto2.ml_en import modelo_filtrado_en


def proyecto2en():
    st.title("PROJECT 2: CREATION OF A ML'S MODEL TO DETECT IF A MUSHROOM IS POISONOUS OR EDIBLE")
    st.markdown(
        '<div style="text-align: justify;">Based on the UCI Machine Learning Repository DataFrame, we began to carry out our second project</p></div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify;">After a study of the parts and characteristics that make up a mushroom, and the information found in the Dataset, we carried out the EDA and preprocessing of the data. We divide the data analysis by the parts that make up the mushroom, for a better explanation of them.</p></div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify;">At the EDA we realized that some characteristics had a great weight when predicting the result, which was confirmed when testing the different Machine Learning classification models, where most of the models gave 100% for both Accuracy, Precision and Recall</p></div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify;">That made us review the project to give a little more value to it, and we decided to check for each type of characteristic what its precision would be. To make the prediction we use the RandomForest model. We encourage you to choose between the different options to check whether a 🍄 is edible or poisonous</p></div>',
        unsafe_allow_html=True)

    st.subheader("ML'S MODEL: MUSHROOMS, ¿EDIBLES O POISONOUS?")

    df = pd.read_csv("proyecto2/mushrooms_eda.csv").drop('CLASS', axis=1)
    df2 = pd.read_csv("proyecto2/mushrooms_eda.csv")

    with st.expander(label="DataFrame", expanded=False):
        st.dataframe(df2)

    cap = [x for x in df.columns if 'CAP' in x]

    gill = [x for x in df.columns if 'GILL' in x]

    stalk = [x for x in df.columns if 'STALK' in x]

    other = [x for x in df.columns if not any(y in x for y in ('CAP', 'GILL', 'STALK'))]

    datos = []
    seleccion = []

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header('CAP')
        # Cap
        for column in df[cap].columns.to_list():
            dato_sombrero = ["All"] + list(df[column].unique())
            sombreros = st.selectbox(label= f"{column}",
                             options=dato_sombrero,
                             index=0)
            datos.append(f"{column}" if sombreros != "All" else None)
            if sombreros !='All':
                seleccion.append(sombreros)

    with col2:
        st.header('GILL')
        # Laminas
        for column in df[gill].columns.to_list():
            dato_laminas = ["All"] + list(df[column].unique())
            laminas = st.selectbox(label=f"{column}",
                         options=dato_laminas,
                         index=0)
            datos.append(f"{column}" if laminas != "All" else None)
            if laminas !='All':
                seleccion.append(laminas)

    with col3:
        st.header('STALK')
        # Tallo
        for column in df[stalk].columns.to_list():
            dato_tallo = ["All"] + list(df[column].unique())
            tallos = st.selectbox(label=f"{column}",
                         options=dato_tallo,
                         index=0)
            datos.append(f"{column}" if tallos != "All" else None)
            if tallos !='All':
                seleccion.append(tallos)

    with col1:
        st.header('OTHERS DATA-1')
        for column in df[other[:3]].columns.to_list():
            dato_otros = ["All"] + list(df[column].unique())
            otros_1 = st.selectbox(label=f"{column}",
                         options=dato_otros,
                         index=0)
            datos.append(f"{column}" if otros_1 != "All" else None)
            if otros_1 !='All':
                seleccion.append(otros_1)

    with col2:
        st.header('OTHERS DATA-2')
        for column in df[other[4:]].columns.to_list():
            dato_otros = ["All"] + list(df[column].unique())
            otros_2 = st.selectbox(label=f"{column}",
                         options=dato_otros,
                         index=0)
            datos.append(f"{column}" if otros_2 != "All" else None)
            if otros_2 !='All':
                seleccion.append(otros_2)

    prediccion = tuple([x for x in datos if not x == None])
    prediccion_list = [x for x in datos if not x == None]
    with open('proyecto2/dicc_en.pkl', 'rb') as file:
        diccionario = pickle.load(file)

    col3.header('PREDICTION')
    if prediccion == ():
        col3.write("Choose an option")
    else:
        test = []
        for datos, valor in zip(prediccion, seleccion):
            test.append(diccionario[datos][valor])

        test = np.array([test])

        test = modelo_filtrado_en(prediccion)[1].transform(test)
        model = modelo_filtrado_en(prediccion)[0]
        y_pred = model.predict(test)
        for k, v in diccionario['CLASS'].items():
            if v == y_pred[0]:
                resultado = k
        if resultado == 'edible':
            col3.metric("PREDICTION", f'{resultado}'.upper())
        else:
            col3.metric("PREDICTION", f'{resultado}'.upper())

        col3.metric("ACCURACY", modelo_filtrado_en(prediccion)[2])
        col3.metric("PRECISSION", modelo_filtrado_en(prediccion)[3])
        col3.metric("RECALL", modelo_filtrado_en(prediccion)[4])

if __name__ == "__main__":
    proyecto2en()