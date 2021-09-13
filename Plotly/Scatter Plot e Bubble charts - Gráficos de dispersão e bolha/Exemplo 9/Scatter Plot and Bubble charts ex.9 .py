import plotly.graph_objects as px # Biblioteca usada para criar gráficos
import numpy as np

np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)
# Cria o objeto com os dados de x e y
fig = px.Figure(data=[px.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers',
     marker=dict(
       color = [10, 20, 30, 50],
       size = [10, 30, 50, 80],
       showscale=True
     )
)]) 
fig.show() # Plota o gráfico

# plotly.express pode criar toda a fígura de uma só vez. Ele usa a graph_objects internamente
