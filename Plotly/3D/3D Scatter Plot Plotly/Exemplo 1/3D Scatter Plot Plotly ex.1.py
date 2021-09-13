import plotly.express as px # Biblioteca usada para criar gráficos

df = px.data.iris() # DataFrame com conjunto de dados iris
fig = px.scatter_3d(df, x = 'sepal_width',
                    y = 'sepal_length',
                    z = 'petal_width',
                    color = 'species')  # Cria o objeto com os dados de x e y.
fig.show() # Plota o gráfico

# plotly.express pode criar toda a fígura de uma só vez. Ele usa a graph_objects internamente
