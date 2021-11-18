import plotly.express as px # Biblioteca usada para criar gráficos
import plotly.graph_objects as go

df = px.data.iris() # DataFrame com conjunto de dados iris
fig = go.Figure(data =[go.Scatter3d(x = df['sepal_width'],
                                   y = df['sepal_length'],
                                   z = df['petal_length'],
                                   mode ='markers',
                                   marker = dict(
                                     size = 12,
                                     color = df['petal_width'],
                                     colorscale ='Viridis',
                                     opacity = 0.8
                                   )
)])  # Cria o objeto com os dados de x e y automaticamente por plotly.
fig.show() # Plota o gráfico

# plotly.express pode criar toda a fígura de uma só vez. Ele usa a graph_objects internamente