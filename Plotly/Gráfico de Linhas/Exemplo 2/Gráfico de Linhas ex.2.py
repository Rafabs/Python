import numpy as np # biblioteca que suporta o processamento de grandes, multi-dimensionais arranjos e matrizes
import plotly.graph_objects as go # Biblioteca usada para criar gráficos

Dias = [1,2,3,4,5]
Temperatura = [20,15,17,35,5]
fig = go.Figure(data=go.Scatter(x = Dias, y = Temperatura)) # O objeto será traçado por uma linha com as info dos eixo x e y.
fig.show() # Plota o gráfico

# plotly.express pode criar toda a fígura de uma só vez. Ele usa a graph_objects internamente