import streamlit as st
from proyecto3.emociones import emociones

def proyecto3():
    st.title("PROYECTO 3: RED NEURONAL DE SENTIMIENTOS")
    st.markdown(
        '<div style="text-align: justify;">A la hora de plantearnos el tercer proyecto, teníamos claro que queríamos realizar una Red Neuronal. La idea que más nos interesaba era crear un modelo donde se pudieran detectar las emociones. Uno de los usos que le vemos es comprobar cuales son las emociones detectadas en un grupo durante una clase de 4 horas ;)</p></div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify;">Empezamos nuestro modelo utilizando varios datasets de imagénes de Kaggle, pero los primeros pasos eran dificiles. Tanto las graficas de accuracy como de pérdida nos daban mucho overfitting al principio. </p><p> Finalmente cogimos varios datasets de imagénes, llegando a trabajar con 27.441 imagénes.</p></div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify;">Por otro lado, vimos la posibilidad de utilizar la función de Streamlit de camara, para crear un acceso facial a nuestra app. Buscamos las fotos de los compañeros y profesores para realizar otro modelo en el que pudieran acceder al proyecto sacando una foto</p></div>',
        unsafe_allow_html=True)
    st.page_link("https://camaraprueba-nyki6ixzgfbvcjgru7kjzf.streamlit.app/", label="FaceID", icon="🔒")

    tab1, tab2, = st.tabs("FOTO EMOCIONES", "VIDEO EMOCIONES")
    with tab1:
        emociones()


if __name__ == "__main__":
        proyecto3()