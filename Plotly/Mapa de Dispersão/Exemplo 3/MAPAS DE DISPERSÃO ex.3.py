# Mapa dos aeroportos dos EUA

import plotly.graph_objects as go # chama o módulo como go para a biblioteca 
import pandas as pd # Biblioteca usada para criar dataframes

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_us_airport_traffic.csv') # Cria o dataframe com os dados do arquivo 'linkado'

# Cria o texto com dados do dataframe
df['text'] = df['airport'] + '' + df['city'] + ', ' + df['state'] + '' + 'Arrivals: ' + df['cnt'].astype(str) 

# Cria a figura do tipo go.Figure
fig = go.Figure(data=go.Scattergeo(
        lon = df['long'], # Variável para dados de Longitude
        lat = df['lat'], # Variável para dados de Latitude
        text = df['text'], # Variável para dados de texto
        mode = 'markers', # Modo dos dados 
        marker_color = df['cnt'], # As cores serão definidas pela diferença de daods da coluna 'cnt' do dataframe
        ))

# Mais alguns detalhes do layout
fig.update_layout(
        title = 'Most trafficked US airports<br>(Hover for airport names)', # Título do layout
        geo_scope='usa', # Foca o mapa nos EUA.
    )
fig.show() # Plota o gráfico