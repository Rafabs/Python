import plotly.figure_factory as ff # Biblioteca usada para criar gráficos
import numpy as np

feature_x = np.arange(0, 50, 2) # Valores do eixo X
feature_y = np.arange(0, 50, 3) # Valores do eixo Y
[X, Y] = np.meshgrid(feature_x, feature_y) # Cria a grade 2D
Z = np.cos(X / 2) + np.sin(Y / 4)
fig = ff.create_annotated_heatmap(Z)
fig.show() # Plota o gráfico

# plotly.express pode criar toda a fígura de uma só vez. Ele usa a graph_objects internamente
# long-form data é adequado para armazenar e exibir dados multivariados, ou seja, com dimensões superiores a 2.