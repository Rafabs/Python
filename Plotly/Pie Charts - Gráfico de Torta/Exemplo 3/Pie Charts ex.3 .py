import plotly.express as px # Biblioteca usada para criar gráficos

df = px.data.iris()
fig = px.pie(df, values="sepal_width",
             names="species",
             color_discrete_sequence=px.colors.sequential.RdBu)   # Cria o objeto com os dados de x e y
fig.show() # Plota o gráfico

# plotly.express pode criar toda a fígura de uma só vez. Ele usa a graph_objects internamente