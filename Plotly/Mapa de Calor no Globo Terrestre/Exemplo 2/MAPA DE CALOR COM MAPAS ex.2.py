import pandas as pd # Biblioteca usada para criação de dataframe

quakes = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/earthquakes-23k.csv') # Cria o dataframe com dados do arquivo

import plotly.graph_objects as go # Chama o módulo go

# Cria a figura e suas configurações
fig = go.Figure(go.Densitymapbox(lat=quakes.Latitude, lon=quakes.Longitude, z=quakes.Magnitude, # Chama os dados de lat/long
                                 radius=10))
fig.update_layout(mapbox_style="stamen-terrain", mapbox_center_lon=180) # Adiciona no layout o estilo do mapa
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}) # Configura no layout as proporções
fig.show() # Plota o gráfico