# Mapa de Precipitação norte-americano

import plotly.graph_objects as go # chama o módulo como go para a biblioteca 
import pandas as pd # Biblioteca usada para criar dataframes

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2015_06_30_precipitation.csv') # Cria o dataframe com os dados do arquivo 'linkado'

# Escala de cores de acordo com os graus de precipitação
scl = [0,"rgb(150,0,90)"],[0.125,"rgb(0, 0, 200)"],[0.25,"rgb(0, 25, 255)"],\
[0.375,"rgb(0, 152, 255)"],[0.5,"rgb(44, 255, 150)"],[0.625,"rgb(151, 255, 0)"],\
[0.75,"rgb(255, 234, 0)"],[0.875,"rgb(255, 111, 0)"],[1,"rgb(255, 0, 0)"]

# Cria a figura do tipo go
fig = go.Figure(data=go.Scattergeo( # Configura a figura como dispersão
    lat = df['Lat'], # variável para os dados de latitude 
    lon = df['Lon'], # variável para os dados de longitude
    text = df['Globvalue'].astype(str) + ' inches', # Configuração do texto Exibido ao passar o mouse
    # Configurando os marcadores
    marker = dict(
        color = df['Globvalue'], # As cores serão separadas pelos dados de 'Globvalue'
        colorscale = scl, # A escala de cor será a da variável scl
        reversescale = True, 
        opacity = 0.7, # Config. de opacidade
        size = 2, # Config. do tamanho dos marcadores
        # Configurando a barra (legenda)
        colorbar = dict( 
            titleside = "right", # Os títulos ficarão a direita da figura
            outlinecolor = "rgba(68, 68, 68, 0)", # Cor da linha out
            ticks = "outside", 
            showticksuffix = "last",
            dtick = 0.1
        )
    )
))

# Mais alguns detalhes do layout
fig.update_layout(
    # Configurando os dados geográficos do mapa
    geo = dict( 
        scope = 'north america', # O escopo serão dos EUA
        showland = True, # Exibe a "terra" de fundo
        landcolor = "rgb(212, 212, 212)", # Cor da "terra"
        subunitcolor = "rgb(255, 255, 255)",
        countrycolor = "rgb(255, 255, 255)",
        showlakes = True,
        lakecolor = "rgb(255, 255, 255)",
        showsubunits = True,
        showcountries = True,
        resolution = 50,
        projection = dict(
            type = 'conic conformal',
            rotation_lon = -100
        ),
        lonaxis = dict(
            showgrid = True,
            gridwidth = 0.5,
            range= [ -140.0, -55.0 ],
            dtick = 5
        ),
        lataxis = dict (
            showgrid = True,
            gridwidth = 0.5,
            range= [ 20.0, 60.0 ],
            dtick = 5
        )
    ),
    title='US Precipitation 06-30-2015<br>Source: <a href="http://water.weather.gov/precip/">NOAA</a>', # Título do mapa
)

fig.show() # Plota o gráfico