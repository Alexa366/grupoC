import streamlit as st
from proyecto3.detectar_emociones import detectar_emociones

def emociones():
    st.subheader("COMPROBACION DE EMOCIONES SEGUN UNA IMAGEN")
    st.markdown(
        '<div style="text-align: justify;">Ya sea subiendo una foto, como sacandoos una, podéis comprobar la emoción detectada.</p></div>',
        unsafe_allow_html=True)
    opciones = ("Subir Foto", "Sacar Foto")
    version = st.radio(label="ELIGE UNA OPCION", options=opciones, horizontal=True)
    if version == "Subir Foto":
        st.button("Subir Foto", type="secondary", use_container_width=True)
        subida = st.file_uploader("FOTO", type=['png', 'jpg'])
        detectar_emociones(subida)
    if version == 'Sacar Foto':
        camara = st.camera_input("Take a picture", key="FirstCamara",help="Saca una foto de tu cara para poder acceder")
        detectar_emociones(camara)

if __name__ == "__main__":
    emociones()