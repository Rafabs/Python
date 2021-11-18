import plotly.graph_objects as go # Biblioteca usada para criar gráficos
import pandas as pd # Biblioteca usada para criar dataframe

# Cria o dataframe
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv') # Utiliza os dados lidos no arquivo

fig = go.Figure(data=[go.Table( # Cria a Tabela

    # Configuração do cabeçalho
    header=dict(values=list(df.columns), # Utiliza os dados do dataframe (df) nas linhas de acordo com a coluna
                fill_color='paleturquoise', # Configuração da cor de preenchimento
                align='left'), # Posiciona o texto

    # Configuração das células
    cells=dict(values=[df.Rank, df.State, df.Postal, df.Population], # Utiliza os dados do dataframe (df) nas colunas
               fill_color='lavender', # Configuração da cor de preenchimento
               align='left')) # Posiciona o texto
])

fig.show() # Plota o gráfico

# plotly.express pode criar toda a fígura de uma só vez. Ele usa a graph_objects internamente