import streamlit as st
import numpy as np
import cv2
from keras.models import load_model
def emociones():

    modelo = load_model('proyecto3.keras')
    tamaño=(64, 64)
    emociones= ['Feliz', 'Neutro', 'Triste']
    prueba = st.camera_input("Take a picture", key="FirstCamara",help="Saca una foto de tu cara para poder acceder")
    if prueba:
        bytes_data = prueba.getvalue()
        image2 = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_GRAYSCALE)
        image2_resize = cv2.resize(image2, dsize=tamaño)
        image_np = np.array(image2_resize)
        img_array = np.expand_dims(image_np, axis=0)
        prediction = modelo.predict(img_array)
        maximo = prediction.max()
        medio = prediction[0][1]
        minimo = prediction.min()
        posicion1 = np.where(prediction == maximo)[1][0]
        posicion2 = np.where(prediction == medio)[1][0]
        posicion3 = np.where(prediction == minimo)[1][0]
        col1, col2 =st.columns(2)
        col1.image(prueba)
        col2.metric(emociones[posicion1].upper(), f"{round(maximo*100,2)}%")
        col2.metric(emociones[posicion2].upper(), f"{round(medio*100,2)}%")
        col2.metric(emociones[posicion3].upper(), f"{round(minimo*100,2)}%")

if __name__ == "__main__":
    emociones()