import plotly.io as pio
import pandas as pd


df = pd.read_csv("https://plotly.com/~public.health/17.csv") # Cria o dataframe com dados do arquivo 'linkado'

data = [dict(
  x = df['date'], # Variável de nomes para o eixo X
  autobinx = False, # Desativa os binnings do eixo x
  autobiny = True, # Ativa os binnings do eixo y
  marker = dict(color = 'rgb(68, 68, 68)'), # Configura a cor da barra/objeto
  name = 'date', # Cria a variável com a coluna de date do csv
  type = 'histogram', # Configura o tipo de gráfico 
  
  # Configurações de dados do Eixo X
  xbins = dict(
    end = '2016-12-31 12:00', # Último dado do gráfico
    size = 'M1', 
    start = '1983-12-31 12:00' # Primeiro dado do gráfico
  )
)]

# Cria o layout
layout = dict(
  paper_bgcolor = 'rgb(240, 240, 240)', # Cor de fundo no papel (tela)
  plot_bgcolor = 'rgb(240, 240, 240)', # Cor de fundo 
  title = '<b>Shooting Incidents</b>', # Título do gráfico

  # Dados a serem plotados no Eixo X
  xaxis = dict(
    title = '',
    type = 'date'
  ),

  # Dados a serem plotados no Eixo Y
  yaxis = dict(
    title = 'Shootings Incidents',
    type = 'linear'
  ),

  # Configuração de distanciamento
  updatemenus = [dict(
        x = 0.1,
        y = 1.15,
        xref = 'paper',
        yref = 'paper',
        yanchor = 'top',
        active = 1,
        showactive = True,

        # Configuração do botão
        buttons = [
        dict(
            args = ['xbins.size', 'D1'],
            label = 'Day',
            method = 'restyle',
        ), dict(
            args = ['xbins.size', 'M1'],
            label = 'Month',
            method = 'restyle',
        ), dict(
            args = ['xbins.size', 'M3'],
            label = 'Quater',
            method = 'restyle',
        ), dict(
            args = ['xbins.size', 'M6'],
            label = 'Half Year',
            method = 'restyle',
        ), dict(
            args = ['xbins.size', 'M12'],
            label = 'Year',
            method = 'restyle',
        )]
  )]
)

fig_dict = dict(data=data, layout=layout) # Cria a fígura

pio.show(fig_dict, validate=False) # Plota o gráfico