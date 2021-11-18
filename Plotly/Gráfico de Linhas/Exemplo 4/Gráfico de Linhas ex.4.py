import plotly.express as px # Biblioteca usada para criar gráficos

df = px.data.iris().head(20) # DataFrame com conjunto de dados Iris
fig = px.line(df, x = "sepal_width", # Cria o objeto com os dados de x e y automaticamente por plotly.
              y = "sepal_length" ,
              color = "sepal_length")
fig.show() # Plota o gráfico

# plotly.express pode criar toda a fígura de uma só vez. Ele usa a graph_objects internamente