# Linhas em Mapbox em Python

import pandas as pd # Biblioteca usada para criar dataframes

us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv") # Lê os dados da planilha
us_cities = us_cities.query("State in ['New York', 'Ohio']") # faz a requisição dos estados mencionados

import plotly.express as px # chama o módulo como px para a biblioteca 

# Cria a figura (mapa) e traça uma linha
# As linhas traças são com base nos estados mencionados
# Cria variáveis de lat/long
# As cores são separadas com bases nos estados
# Configuração de zoom e altura
fig = px.line_mapbox(us_cities, lat="lat", lon="lon", color="State", zoom=3, height=300) 

# Adiciona o layout do mapa
# Configura o estilo do mapa
# Configura o zoom de exibição
# centraliza a latitude
fig.update_layout(mapbox_style="stamen-terrain", mapbox_zoom=4, mapbox_center_lat = 41,
    margin={"r":0,"t":0,"l":0,"b":0})

fig.show() # Plota o gráfico