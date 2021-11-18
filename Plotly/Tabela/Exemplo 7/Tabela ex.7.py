import plotly.graph_objects as go # Biblioteca usada para criar gráficos
from plotly.colors import n_colors # Biblioteca usada para configurações detalhadas de cores no gráfico
import numpy as np # Biblioteca usada para trabalhos com números

np.random.seed(1)
# Configuração das cores de cada linhas, separadas por [],[],[],...[]
colors = n_colors('rgb(255, 200, 200)', 'rgb(200, 0, 0)', 9, colortype='rgb')
# Variáveis para criação de dados nas configurações:
a = np.random.randint(low=0, high=9, size=10)
b = np.random.randint(low=0, high=9, size=10)
c = np.random.randint(low=0, high=9, size=10)

# Cria a tabela
fig = go.Figure(data=[go.Table(
  # Configuração do cabeçalho
  header=dict(
    values=['<b>Column A</b>', '<b>Column B</b>', '<b>Column C</b>'], # Títulos das colunas
    line_color='white', fill_color='white', # Cor da linha e preenchimento
    align='center',font=dict(color='black', size=12) # Configuração de alinhamento de texto cor e tamanho
  ),
  cells=dict(
    # Configuração do linhas
    values=[a, b, c], # Dados das linhas
    line_color=[np.array(colors)[a],np.array(colors)[b], np.array(colors)[c]], # Cor da linha
    fill_color=[np.array(colors)[a],np.array(colors)[b], np.array(colors)[c]], # Cor do preenchimento
    align='center', font=dict(color='white', size=11) # Configuração de alinhamento de texto cor e tamanho
    ))
])

fig.show() # Plota o gráfico

# plotly.express pode criar toda a fígura de uma só vez. Ele usa a graph_objects internamente