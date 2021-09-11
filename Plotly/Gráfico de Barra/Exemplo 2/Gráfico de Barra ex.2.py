import plotly.express as px # Biblioteca usada para criar gráficos
import numpy as np

np.random.seed(42)
random_x = np.random.randint(1, 101, 100) # Eixo x, cria 100 números aleatórios variando de 0 a 100 no intervalo de 1.
random_y = np.random.randint(1, 101, 100) # Eixo y, cria 100 números aleatórios variando de 0 a 100 no intervalo de 1.

fig = px.bar(random_x, y = random_y) # Cria o objeto com os dados de x e y
fig.show() # Plota o gráfico

# plotly.express pode criar toda a fígura de uma só vez. Ele usa a graph_objects internamente