import plotly.graph_objects as go # Biblioteca usada para criar gráficos

fig = go.Figure() # Cria a classe mais genérica de go.Barplotly.graph_objects
fig.add_trace(go.Bar( # Adiciona um traço no gráfico de barras
    y=['giraffes', 'orangutans', 'monkeys'], # Eixo Y
    x=[20, 14, 23], # Eixo X
    name='SF Zoo', # Nome do traço
    orientation='h', # Orientação
    # Config. de cor e Largura
    marker=dict(
        color='rgba(246, 78, 139, 0.6)', 
        line=dict(color='rgba(246, 78, 139, 1.0)', width=3)
    )
))
fig.add_trace(go.Bar( # Adiciona um traço no gráfico de barras
    y=['giraffes', 'orangutans', 'monkeys'], # Eixo Y
    x=[12, 18, 29], # Eixo X
    name='LA Zoo', # Nome do traço
    orientation='h', # Orientação
    # Config. de cor e Largura
    marker=dict(
        color='rgba(58, 71, 80, 0.6)',
        line=dict(color='rgba(58, 71, 80, 1.0)', width=3)
    )
))

fig.update_layout(barmode='stack') # barmode = ‘stack’ = As barras serão
fig.show() # Plota o gráfico