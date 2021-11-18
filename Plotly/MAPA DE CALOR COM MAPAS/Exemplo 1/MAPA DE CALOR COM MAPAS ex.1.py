import pandas as pd # Biblioteca usada para criação de dataframe

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/earthquakes-23k.csv') # Cria o dataframe com dados do arquivo

import plotly.express as px # Chama o módulo px

# Cria a figura e suas configurações
fig = px.density_mapbox(df, lat='Latitude', lon='Longitude', z='Magnitude', radius=10, # Chama o dataframe, dados de lat/long
                        center=dict(lat=0, lon=180), zoom=0, 
                        mapbox_style="stamen-terrain")
fig.show() # Plota o gráfico