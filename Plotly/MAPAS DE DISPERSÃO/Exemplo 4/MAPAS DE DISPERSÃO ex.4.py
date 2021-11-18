# Mapa dos aeroportos dos EUA

import plotly.graph_objects as go # chama o módulo como go para a biblioteca 
import pandas as pd # Biblioteca usada para criar dataframes

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_us_airport_traffic.csv') # Cria o dataframe com os dados do arquivo 'linkado'

# Cria o texto com dados do dataframe
df['text'] = df['airport'] + '' + df['city'] + ', ' + df['state'] + '' + 'Arrivals: ' + df['cnt'].astype(str) 

# Cria a figura do tipo go.Figure
fig = go.Figure(data=go.Scattergeo(
        locationmode = 'USA-states', # Filtra os Estados dos EUA
        lon = df['long'], # Variável para dados de Longitude
        lat = df['lat'], # Variável para dados de Latitude
        text = df['text'], # Variável para dados de texto
        mode = 'markers', # Modo dos dados 
        # Configuração do fundo do mapa
        marker = dict( 
            size = 8, # Tamanho
            opacity = 0.8, # Opacidade
            reversescale = True, # Escala reversa
            autocolorscale = False, # Autoescala DESATIVADA
            symbol = 'square', # usa o símbolo (pontos) do tipo 'square'/quadrado
            # Configuração das linhas divisórias 
            line = dict(
                width=1, # largura
                color='rgba(102, 102, 102)' # Cor por código RGB
            ),
            colorscale = 'Blues', # Escala de cor 'Blues', tons de azul
            cmin = 0, # Configurações de cores com número mínimos (menores) da tabela
            color = df['cnt'], # As cores serão definidas pela diferença de daods da coluna 'cnt' do dataframe
            cmax = df['cnt'].max(), # Configurações de cores com número máximos (maiores) da tabela
            colorbar_title="Incoming flights<br>February 2011" # Título da escala de cor 
        )))

# Mais alguns detalhes do layout
fig.update_layout(
        title = 'Most trafficked US airports<br>(Hover for airport names)', # Título do mapa
        # Configuração do mapa
        geo = dict(
            scope='usa', # Foca o mapa nos EUA
            projection_type='albers usa', # Tipo de projeção do mapa para os EUA
            showland = True, # Exibe a "terra" de fundo
            landcolor = "rgb(250, 250, 250)", # Cor da "terra"
            subunitcolor = "rgb(217, 217, 217)", 
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = 0.5,
            subunitwidth = 0.5
        ),
    )
fig.show() # Plota o gráfico