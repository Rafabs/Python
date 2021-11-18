import plotly.graph_objects as go # Biblioteca usada para criar gráficos
import pandas as pd # Biblioteca usada para criar dataframe

# Configuração das cores de cada linhas, separadas por [],[],[],...[]
colors = ['rgb(239, 243, 255)', 'rgb(189, 215, 231)', 'rgb(107, 174, 214)', 'rgb(49, 130, 189)', 'rgb(8, 81, 156)']
data = {'Year' : [2010, 2011, 2012, 2013, 2014], 'Color' : colors} # Variável para dados das linhas
df = pd.DataFrame(data) # cria o dataframe com os dados da variável

# Cria a tabela
fig = go.Figure(data=[go.Table(
  # Configuração do cabeçalho
    header=dict(
        values=["Color", "<b>YEAR</b>"], # Títulos das colunas
        line_color='white', fill_color='white', # Cor da linha e preenchimento
        align='center', font=dict(color='black', size=12) # Configuração de alinhamento de texto cor e tamanho
    ),
  # Configuração do linhas
    cells=dict(
        values=[df.Color, df.Year], # Dados das linhas
        line_color=[df.Color], fill_color=[df.Color], # Cor da linha e preenchimento
        align='center', font=dict(color='black', size=11)))]) # Configuração de alinhamento de texto cor e tamanho

fig.show() # Plota o gráfico

# plotly.express pode criar toda a fígura de uma só vez. Ele usa a graph_objects internamente