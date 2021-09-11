import plotly.express as px # Biblioteca usada para criar gráficos

long_df = px.data.medals_long() # DataFrame com conjunto de dados com a variável do tipo long
fig = px.bar(long_df, x = "nation", y = "count",
             color = "medal", title = "Long-Form Input") # Cria o objeto com os dados de x e y
fig.show() # Plota o gráfico

# plotly.express pode criar toda a fígura de uma só vez. Ele usa a graph_objects internamente
# long-form data é adequado para armazenar e exibir dados multivariados, ou seja, com dimensões superiores a 2.
