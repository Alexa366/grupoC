import streamlit as st
from inicio.inicio import inicio
from proyecto1.proyecto_inicio import proyecto
from proyecto2.proyecto2_es import proyecto2es
from proyecto2.proyecto2_en import proyecto2en


def main():
    menu = ["BOOTCAMP DSB05RT", "PROYECTO 1 - ALIMENTOS", "PROYECTO 2 - SETAS", "PROYECTO 3 - EMOCIONES"]

    seleccion = st.sidebar.selectbox(label="Menu", options=menu)

    if seleccion == "BOOTCAMP DSB05RT":
        inicio()

    if seleccion == "PROYECTO 1 - ALIMENTOS":
        proyecto()


    if seleccion == "PROYECTO 2 - SETAS":
        # Make
        versiones = ("Spanish Version", "English Version")
        version = st.sidebar.radio(label="Version", options=versiones)
        if version == "Spanish Version":
            proyecto2es()
        elif version == "English Version":
            proyecto2en()


if __name__ == "__main__":
    main()

