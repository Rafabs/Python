# Linhas nos mapas do Mapbox usando traços Scattermapbox

import plotly.graph_objects as go

# Cria a figura (mapa) e cria os pontos de dispersões
fig = go.Figure(go.Scattermapbox(
    mode = "markers+lines", # O modo marcador + linha traça uma linha com circulos nas extremidades
    lon = [10, 20, 30], # Variável de longitude
    lat = [10, 20,30], # Variável de latitude
    marker = {'size': 10})) # Dimensionamento do marcador

# Adiciona um traço a figura (mapa) e cria os pontos de dispersões
fig.add_trace(go.Scattermapbox(
    mode = "markers+lines", # O modo marcador + linha traça uma linha com circulos nas extremidades
    lon = [-50, -60,40], # Variável de longitude
    lat = [30, 10, -20], # Variável de latitude
    marker = {'size': 10})) # Dimensionamento do marcador

# Cria um layout a figura (mapa)
fig.update_layout(
    margin ={'l':0,'t':0,'b':0,'r':0}, # Config. de margens
    #  Config. do mapa
    mapbox = {
        'center': {'lon': 10, 'lat': 10},
        'style': "stamen-terrain",
        'center': {'lon': -20, 'lat': -20},
        'zoom': 1})

fig.show() # Plota o gráfico