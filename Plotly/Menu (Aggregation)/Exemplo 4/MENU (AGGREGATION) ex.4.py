import plotly.io as pio
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/bcdunbar/datasets/master/worldhappiness.csv") # Cria o dataframe com dados do arquivo 'linkado'

aggs = ["count","sum","avg","median","mode","rms","stddev","min","max","first","last"] # Configura os nomes dos filtros

agg = [] # Configura os filtros como lista
agg_func = [] # Configura os filtros como lista


for i in range(0, len(aggs)):
    agg = dict(
        args=['transforms[0].aggregations[0].func', aggs[i]],
        label=aggs[i],
        method='restyle'
    )
    agg_func.append(agg)


# Cria o conjunto de dados
data = [dict(
  type = 'choropleth', # Tipo Mapa coroplético 'choropleth'
  locationmode = 'country names', # Variável para nomes dos países 'country names'
  locations = df['Country'], # Variável do dataframe de filtro dos países 'Country' 
  z = df['HappinessScore'], # Variável do dataframe de filtro dde Pontuação da Felicidade 'HappinessScore'
  autocolorscale = False, # Escala de cor automática desativada
  colorscale = 'Portland', # Tipo de escala de cor
  reversescale = True, # Escala reversa ativada (do menor, menos intenso para o maior, mais intenso)

  # Configuração dos dados agrupados
  transforms = [dict(
    type = 'aggregate', # Tipo de dados
    groups = df['Country'], # Dados a serem agrupados
    aggregations = [dict( # Configuração dos dados agrupados
        target = 'z', func = 'sum', enabled = True)
    ]
  )]
)]

# Cria o layout
layout = dict(
  title = '<b>Plotly Aggregations</b><br>use dropdown to change aggregation', # Título do gráfico
  xaxis = dict(title = 'Subject'), # Configuração de dados do Eixo X
  yaxis = dict(title = 'Score', range = [0,22]), # Configuração de dados do Eixo Y
  height = 600, # Altura
  width = 900, # Largura

  # Configuração do menu e dos dados
  updatemenus = [dict(
        x = 0.85,
        y = 1.15,
        xref = 'paper',
        yref = 'paper',
        yanchor = 'top',
        active = 1,
        showactive = False,
        buttons = agg_func
  )]
)

fig_dict = dict(data=data, layout=layout) # Cria a fígura

pio.show(fig_dict, validate=False) # Plota o gráfico