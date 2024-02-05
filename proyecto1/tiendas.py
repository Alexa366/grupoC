import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
import folium
import requests
import json


def tiendas():
    st.header('BUSCADOR DE TIENDAS POR CATEGORIA')

    df = pd.read_csv('datos_tiendas.csv')

    lista_categorias = df['Categorias'].value_counts().head(10).reset_index()['Categorias'].tolist()

    categorias = st.selectbox(label="Categorias",
                                            options=lista_categorias)

    tiendas = df[df['Categorias'] == categorias].head(10)['Tiendas'].head(5).tolist()

    provincias_geo = "provincias-espanolas .geojson"
    with open(provincias_geo) as json_file:
        info = json.load(json_file)

    datos_provincias = {}

    provincias = [x['properties']['provincia'] for x in info['features']]
    coordenadas = [x['properties']['geo_point_2d'] for x in info['features']]

    for provincia, coordenada in zip(provincias, coordenadas):
        datos_provincias[provincia] = coordenada

    provincia = st.selectbox(label="Provincias",
                             options=sorted(provincias))

    API_KEY = 'fsq39XJ/xxHyWyLRUAxqo0/f9Yx/IzXcpdmVw/4zqUSCW+E='

    search_url = "https://api.foursquare.com/v3/places/search"

    query = f"{tiendas}"

    lon, lat = datos_provincias[provincia].values()

    endpoint = f"{search_url}?query={query}&ll={lat},{lon}&limit=50"

    headers = {"accept": "application/json",
               "Authorization": API_KEY}


    response = requests.get(url=endpoint, headers=headers)

    data = response.json()

    data_df = list()

    for r in data["results"]:
        fsq_id = r["fsq_id"]
        latitude = r["geocodes"]["main"]["latitude"]
        longitude = r["geocodes"]["main"]["longitude"]
        location = r["location"]["formatted_address"]
        name = r["name"]

        data_df.append([name, latitude, longitude, location, fsq_id])

    df_lugares = pd.DataFrame(data=data_df, columns=["name", "latitude", "longitude", "location", "fsq_id"])

    lon = datos_provincias[provincia]['lon']
    lat = datos_provincias[provincia]['lat']
    provincia_map = folium.Map(location=[lat, lon], zoom_start=10)

    supermercados = folium.map.FeatureGroup()

    for lat, lng, name in zip(df_lugares["latitude"], df_lugares["longitude"], df_lugares["name"]):
        supermercados.add_child(folium.Marker(location=[lat, lng],
                                              popup=f"{name}"))

    provincia_map.add_child(supermercados)
    st_folium(provincia_map, use_container_width=True)



if __name__ == "__main__":
    tiendas()