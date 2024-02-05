import streamlit as st


def inicio():
    st.title(body="PROYECTOS REALIZADOS EN DSB05RT :abacus:")

    st.subheader(body="Liuva :female_superhero:, Alex :female_superhero:, David :male_zombie:")

    st.write("Preparense a disfrutar de los proyectos que hemos realizado durante este Bootcamp.")

    st.warning("""Tranquilos, en cinco minutos lo tienen visto.""")

    tab1, tab2, tab3 = st.tabs(["PROYECTO 1 - ALIMENTOS", "PROYECTO 2 - SETAS", "PROYECTO 3 - EMOCIONES"])


if __name__ == "__main__":
    inicio()