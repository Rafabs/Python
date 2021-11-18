import plotly.express as px # Biblioteca usada para criar gráficos

df = px.data.medals_wide() # DataFrame com conjunto de dados de medalhas
fig = px.bar(df, x="nation",
             y=["gold", "silver", "bronze"],
             title="Wide Form Data") # Cria o objeto com os dados de x e y
fig.show() # Plota o gráfico

# plotly.express pode criar toda a fígura de uma só vez. Ele usa a graph_objects internamente
# long-form data é adequado para armazenar e exibir dados multivariados, ou seja, com dimensões superiores a 2.