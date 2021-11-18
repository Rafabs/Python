import plotly.graph_objects as go  # Biblioteca usada para criar gráficos
import numpy as np

data = [[1,2,3,4,5],
        [3,4,5,6,7],
        [7,8,9,6,4],
        [3,7,2,4,2]]

fig = go.Figure(data = go.Contour(z = data)) # Cria o objeto com os dados de x e y automaticamente por plotly.
fig.show() # Plota o gráfico

# plotly.express pode criar toda a fígura de uma só vez. Ele usa a graph_objects internamente