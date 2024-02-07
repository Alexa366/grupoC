import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

def home():
    st.markdown("## Introducción")
    col1, col2 = st.columns(2)

    col1.markdown("## Inicios")

    col1.markdown('<div style="text-align: justify;">Empezamos este BOOTCAMP el lejano 11 de Septiembre (vaya fecha) y ahi comenzamos a aprender términos como iterar, listas, diccionarios. Conocimos a Bárbara, a Fede, nos nombraron a un tal Dani como tutor y conocimos a los compañeros con los que ibamos a sufrir los siguientes meses</p></div>', unsafe_allow_html=True)
    col2.video("https://youtu.be/gscbkGS6Bh8")
    add_vertical_space(1)



if __name__ == "__main__":
    home()