import streamlit as st
from streamlit_option_menu import option_menu
from proyecto1.proyecto_inicio import proyecto
from proyecto2.proyecto2_es import proyecto2es
from proyecto2.proyecto2_en import proyecto2en


def main():
    st.set_page_config(
        page_title="PROYECTOS REALIZADOS EN DSB05RT",
        page_icon=":abacus", )


    st.subheader(body="Liuva :female_superhero:, Alex :female_superhero: y David :male_zombie:")

    st.write("Presentan los proyectos realizados durante este Bootcamp.")

    seleccion = option_menu(
        menu_title=None,
        options=["PROYECTO 1 - ALIMENTOS", "PROYECTO 2 - SETAS", "PROYECTO 3 - EMOCIONES"],
        icons=["1-square", "2-square-fill", "3-square"],
        default_index=0,
        orientation="horizontal", )

    if seleccion == "BOOTCAMP DSB05RT":
        inicio()

    if seleccion == "PROYECTO 1 - ALIMENTOS":
        proyecto()

    if seleccion == "PROYECTO 2 - SETAS":
        # Make
        versiones = ("Spanish Version", "English Version")
        version = st.radio(label="VERSION", options=versiones)
        if version == "Spanish Version":
            proyecto2es()
        elif version == "English Version":
            proyecto2en()


if __name__ == "__main__":
    main()

