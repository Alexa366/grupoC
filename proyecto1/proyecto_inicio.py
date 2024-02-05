import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from proyecto1.buscador import buscador

def proyecto():

    st.title("ESTUDIO DE PRODUCTOS DE ALIMENTACION")

    tab1, tab2, tab3 = st.tabs(["TIENDAS SEGUN ECOSCORE", "MARCAS BLANCAS", "LOCALIZADOR DE TIENDAS"])

    tab1.write("Revisar tiendas")

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

    tab2.write("Marcas Blancas")

    tab2.header('COMPARACION MARCAS vs MARCAS BLANCAS')

    lista_categorias = df['Categorias'].value_counts().head(10).reset_index()['Categorias'].tolist()

    categorias = tab2.selectbox(label="Categorias",
                              options=lista_categorias)

    lista_marcas = df[df['Categorias'] == categorias]['Marcas'].value_counts().head(5).index.tolist()
    marca1 = tab2.selectbox(label="Marca", options=lista_marcas)

    lista_marcas.remove(marca1)

    marca2 = tab2.selectbox(label="Marca", options=lista_marcas)

    df_grafico = df[(df['Marcas'].isin([marca1, marca2])) & (df['Categorias'] == categorias)][
        ['Carbohidratos', 'kcal', 'Grasas', 'Azucares', 'Marcas', 'Categorias']].dropna()
    fig = sns.pairplot(df_grafico, height=2, hue='Marcas')
    plt.suptitle(f'Comparación de {marca1} y {marca2} en la categoría {categorias}', y=1.02)
    tab2.pyplot(fig.fig)

    tab3.write("BUSCADOR DE TIENDAS")
    buscador()




if __name__ == "__main__":
    proyecto()

