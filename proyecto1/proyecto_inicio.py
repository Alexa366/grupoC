import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

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


    tab1, tab2, tab3, tab4 = st.tabs(["TIENDAS SEGUN ECOSCORE", "COMPARACION PRODUCTOS", "Nº DE ADITIVOS Y GRADO DE NUTRICION", "MARCAS BLANCAS"])

    # TIENDAS SEGUN ECOSCORE
    tab1.subheader("REVISION ECOSCORE")

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

    # COMPARACION DE PRODUCTOS SEGUN VALORES ENERGETICOS
    tab2.subheader("COMPARACION DE PRODUCTOS SEGUN VALORES ENERGETICOS")

    tab2.markdown(
        '<div style="text-align: justify;">Creamos una comparativa gráfica de productos según sus valores enérgeticos </p><p> La idea nos surgió de una charla grupal con Bárbara, donde nos pedía elegir entre Pepsi y Coca-Cola, o Nocilla y Nutella. En aquella ocasión era por gustos, no por salud 😉</p></div>',
        unsafe_allow_html=True)

    # Marcas
    marcas = df['Marcas'].dropna().unique()
    marca = tab2.multiselect("MARCAS", marcas, ['Nocilla', 'Nutella'])

    datos = tab2.radio("Elige", ["Grasas", "kcal", "Grasas saturadas", "Azucares"], horizontal=True)

    df_filtrado_marcas = df[df["Marcas"].isin(marca)]
    agrupado = df_filtrado_marcas.groupby("Marcas")[["Grasas", "kcal", "Grasas saturadas", "Azucares"]].mean()
    tab2.dataframe(agrupado[datos], use_container_width=True)
    tab2.bar_chart(agrupado[datos], use_container_width=True,
                   color=(np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255)))

    tab3.subheader("RELACION NUMERO DE ADITIVOS CON EL GRADO DE NUTRICION")
    tab3.markdown(
        '<div style="text-align: justify;">Queremos ver cómo están relacionados los campos grado de nutrición y los aditivos. Para ello creamos un scatterplot.</p></div>',
        unsafe_allow_html=True)
    # Creamos una variable para mapear el campo Nutriscore y poder tratarlo.
    mapa_nutriscore = {"a": 5, "b": 4, "c": 3, "d": 2, "e": 1}
    df_filtrado_tiendas["Nutriscore_nro"] = df_filtrado_tiendas["Nutriscore"].map(mapa_nutriscore)
    # Convertimos la colunma Nutriscor_nro a valor numerico, para que no de error al graficar
    df_filtrado_tiendas['Nutriscore_nro'] = pd.to_numeric(df_filtrado_tiendas['Nutriscore_nro'], errors='coerce')

    # Calcula la media del número de aditivos y el grado de nutrición por Grupo de alimentos en las tiendas seleccionadas anteriormente
    nro_aditivos_media = df_filtrado_tiendas.groupby('Grupo alimentos')['Nro aditivos'].mean()
    nro_grado_nutricion = df_filtrado_tiendas.groupby('Grupo alimentos')['Nutriscore_nro'].mean()

    fig = px.scatter(
        data_frame=df_filtrado_tiendas.iloc[:1000, :],
        y=nro_aditivos_media,
        x=nro_grado_nutricion,
        color=nro_grado_nutricion.index,
        hover_name=nro_aditivos_media.index,
        height=None,
        opacity=0.5
    )

    # Títulos
    fig.update_xaxes(title_text='Grado de Nutrición')
    fig.update_yaxes(title_text='Media de Aditivos')

    # Leyenda
    fig.update_traces(marker=dict(size=5), selector=dict(mode='markers'), showlegend=True)

    # Título principal

    fig.update_layout(title_text="Gráfico de Dispersión entre Nutriscore y media aditivos")

    tab3.plotly_chart(figure_or_data=fig)

    tab3.markdown(
        '<div style="text-align: justify;">Podemos comprobar que la mayoria de las categorías se mueven en un grado de nutrición de entre 2 y 3.5 con una media de aditivos de hasta 5, los alimentos con más nutrición por encima de 4 no superan los 4 aditivos de media..</p></div>',
        unsafe_allow_html=True)


    with tab4:
        tab4.write("MARCAS BLANCAS vs MARCAS TRADICIONALES")
        tab4.markdown(
            '<div style="text-align: justify;">Queremos ver cual eran la diferencia entre los productos de marca blanca y los productos originales, y así comprobar que cual sería la mejor opción en términos de valores energéticos</p></div>',
            unsafe_allow_html=True)
        lista_categorias = df['Categorias'].value_counts().head(10).reset_index()['Categorias'].tolist()

        categorias = tab4.selectbox(label="Categorias",
                                    options=lista_categorias)
        col1, col2 = st.columns(2)
        marcas_blancas = ["Hacendado", "Dia", "Carrefour", "Eroski", "Auchan", "El Corte Ingles"]
        marca_blanca = col2.selectbox(label="Marca Blanca", options=marcas_blancas)

        lista_marcas = df[(df['Categorias'] == categorias)&(~df['Marcas'].isin(marcas_blancas))]['Marcas'].value_counts().head(5).index.tolist()

        marca = col1.selectbox(label="Marca", options=lista_marcas)
        datos2 = tab4.radio("Elige", ["Grasas", "kcal", "Grasas saturadas", "Azucares"], horizontal=True, key="Segunda")

        df_grafico = df[(df['Marcas'].isin([marca_blanca, marca])) & (df['Categorias'] == categorias)][
            ['Carbohidratos', 'kcal', 'Grasas', 'Azucares', 'Marcas', 'Categorias']].dropna()
        fig = sns.pairplot(df_grafico, height=2, hue='Marcas', y_vars=datos2)
        plt.suptitle(f'Comparación de {marca_blanca} y {marca} en la categoría {categorias}', y=1.02)
        tab4.pyplot(fig.fig)

if __name__ == "__main__":
    proyecto()

