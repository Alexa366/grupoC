import streamlit as st
import requests
import json

def lugares(tiendas):
    provincias_geo = "provincias-espanolas .geojson"
    with open(provincias_geo) as json_file:
        info = json.load(json_file)

    st.header('BUSCADOR DE TIENDAS POR CATEGORIA')

    datos_provincias = {}

    provincias = [x['properties']['provincia'] for x in info['features']]
    coordenadas = [x['properties']['geo_point_2d'] for x in info['features']]

    provincia = st.selectbox(label="Provincias",
                              options=provincias)

    for provincia, coordenada in zip(provincias, coordenadas):
        datos_provincias[provincia] = coordenada

    API_KEY = 'fsq39XJ/xxHyWyLRUAxqo0/f9Yx/IzXcpdmVw/4zqUSCW+E='

    search_url = "https://api.foursquare.com/v3/places/search"

    query = f"{tiendas}"

    near = f"{provincia}"

    lon, lat = datos_provincias[provincia].values()

    endpoint = f"{search_url}?query={query}&ll={lat},{lon}&limit=50"

    print(f"Endpoint: {endpoint}")

    headers = {"accept": "application/json",
               "Authorization": API_KEY}
    headers

    response = requests.get(url=endpoint, headers=headers)

    print(f"response: {response.status_code}")

    data = response.json()
    return data

if __name__ == "__main__":
    lugares(tiendas)
