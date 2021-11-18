import plotly.express as px # Biblioteca usada para criar gráficos
import plotly.graph_objects as go #

df = px.data.iris() # DataFrame com conjunto de dados de iris
fig = go.Figure(data=[go.Histogram(x=df['sepal_width'])]) # Cria o objeto com os dados de x
fig.show() # Plota o gráfico

# plotly.express pode criar toda a fígura de uma só vez. Ele usa a graph_objects internamente
# 'Figure' e estes são serializados como JSON antes de ser passado para plotly.js