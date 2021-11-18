import plotly.figure_factory as ff  # Biblioteca usada para criar gráficos

df = [dict(Task="A", Start='2020-01-01', Finish='2009-02-02'), # DataFrame com conjunto de dados
    dict(Task="Job B", Start='2020-03-01', Finish='2020-11-11'),
    dict(Task="Job C", Start='2020-08-06', Finish='2020-09-21')]

fig = ff.create_gantt(df)  # Cria o objeto com os dados de x e y
fig.show() # Plota o gráfico

# plotly.express pode criar toda a fígura de uma só vez. Ele usa a graph_objects internamente
# long-form data é adequado para armazenar e exibir dados multivariados, ou seja, com dimensões superiores a 2.