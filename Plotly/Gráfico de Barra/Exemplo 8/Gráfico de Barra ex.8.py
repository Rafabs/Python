import plotly.express as px # Biblioteca usada para criar gráficos

df = px.data.tips() # DataFrame com conjunto de dados
fig = px.bar(df, x="total_bill", y="day",
             color="sex", barmode = 'stack') # Cria o objeto com os dados de x e y
fig.show() # Plota o gráfico

# plotly.express pode criar toda a fígura de uma só vez. Ele usa a graph_objects internamente
# long-form data é adequado para armazenar e exibir dados multivariados, ou seja, com dimensões superiores a 2.