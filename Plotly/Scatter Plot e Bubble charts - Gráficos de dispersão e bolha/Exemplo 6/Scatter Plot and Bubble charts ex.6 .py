import plotly.graph_objects as go # Biblioteca usada para criar gráficos
import numpy as np

n = 10000
fig = go.Figure(data=[go.Scatter(
    x = np.random.randn(n),
    mode = 'markers',
    marker=dict(
        color=np.random.randn(n),
        colorscale='Viridis',
        showscale=True
    )
)
                     ])  # Cria o objeto com os dados de x e y
fig.show() # Plota o gráfico

# plotly.express pode criar toda a fígura de uma só vez. Ele usa a graph_objects internamente