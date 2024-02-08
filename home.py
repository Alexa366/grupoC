import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

def home():
    st.markdown("## Introducción")
    col1, col2 = st.columns(2)

    col1.markdown("## Inicios")

    col1.markdown('<div style="text-align: justify;">Empezamos este BOOTCAMP el lejano 11 de Septiembre (vaya fecha) y ahi comenzamos a aprender términos como iterar, listas, diccionarios. Conocimos a Bárbara, a Fede, nos nombraron a un tal Dani como tutor y conocimos a los compañeros con los que ibamos a sufrir los siguientes meses</p></div>', unsafe_allow_html=True)
    col2.video("https://youtu.be/gscbkGS6Bh8")
    add_vertical_space(1)

    st.markdown("## Primer Proyecto")
    st.markdown('<div style="text-align: justify;">"Solo" habían pasado dos meses desde el inicio, y ya nos teníamos que poner a hacer nuestro propio proyecto, y en colaboración con el resto de compañeros, que locura!!</p></div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;">Nos imaginamos que, como les pasó al resto de los compañeros, las dudas de en qué aplicar tan "vasto conocimiento" adquirido iban provocando nervios. En nuestro caso, dedicamos nuestro primer proyecto a extraer y analizar los datos de la API de Open Food Facts</p></div>', unsafe_allow_html=True)
    st.page_link("https://es.openfoodfacts.org", label="Open Food facts",icon="🥕","🍔", "🍒", "🍨")
    add_vertical_space(2)
    st.markdown(
        '<div style="text-align: justify;">Las dificultades en este primer proyecto fueron las dudas de si nos daba tiempo a presentar y si eramos capaces de </p></div>',
        unsafe_allow_html=True)


if __name__ == "__main__":
    home()