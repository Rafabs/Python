import plotly.graph_objects as go # Biblioteca usada para criar gráficos

fig = go.Figure(go.Bar(  # Cria a classe mais genérica de go.Barplotly.graph_objects
            x=[20, 14, 23], # Cria o objeto com os dados de x e y na horizontal
            y=['giraffes', 'orangutans', 'monkeys'],
            orientation='h'))

fig.show() # Plota o gráfico