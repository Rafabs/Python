import plotly.graph_objects as go  # Biblioteca usada para criar gráficos
import numpy as np

feature_x = np.arange(0, 50, 2) # Valores do eixo X
feature_y = np.arange(0, 50, 3) # Valores do eixo Y
[X, Y] = np.meshgrid(feature_x, feature_y) # Cria a grade 2D
Z = np.cos(X / 2) + np.sin(Y / 4)
fig = go.Figure(data=go.Contour( # Cria o objeto com os dados de x e y automaticamente por plotly.
    x=feature_x, y=feature_y, z=Z,
    contours=dict(
        coloring='lines',
        showlabels=True,)
))
fig.show() # Plota o gráfico

# plotly.express pode criar toda a fígura de uma só vez. Ele usa a graph_objects internamente