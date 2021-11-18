import plotly.express as px # Biblioteca usada para criar gráficos
import numpy

random_x = [100, 2000, 550]
names = ['A', 'B', 'C']
fig = px.pie(values=random_x, names=names)   # Cria o objeto com os dados de x e y
fig.show() # Plota o gráfico

# plotly.express pode criar toda a fígura de uma só vez. Ele usa a graph_objects internamente