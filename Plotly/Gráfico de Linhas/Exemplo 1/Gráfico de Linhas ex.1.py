import plotly.express as px

Dias = [1,2,3,4,5]
Temperatura = [20,15,17,35,5]
fig = px.line( x = Dias , y = Temperatura, # O objeto será traçado por uma linha com as info dos eixo x e y.
               title = 'Relação de Temperatura dos Primeiros 5 dias') # Título do Gráfico
fig.show() # Plota o gráfico

# plotly.express pode criar toda a fígura de uma só vez. Ele usa a graph_objects internamente