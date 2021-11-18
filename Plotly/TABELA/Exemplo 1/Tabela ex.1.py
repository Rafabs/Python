import plotly.graph_objects as go # Biblioteca usada para criar gráficos

fig = go.Figure(data=[go.Table(header=dict(values=['A Scores', 'B Scores']), # Cria a tabela com cabeçalho de 2 colunas
                 cells=dict(values=[[100, 90, 80, 90], [95, 85, 75, 95]])) # Os valores apresentados,colunas separadas por [],[]...
                     ])
fig.show() # Plota o gráfico

