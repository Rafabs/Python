import plotly.express as px # Biblioteca usada para criar gráficos
import plotly.graph_objects as go #

df = px.data.iris() # DataFrame com conjunto de dados de iris
fig = go.Figure(data=[go.Histogram(y=df['sepal_width'],
                                   cumulative_enabled=True)])   # Cria o objeto
fig.show() # Plota o gráfico

# plotly.express pode criar toda a fígura de uma só vez. Ele usa a graph_objects internamente
# 'Figure' e estes são serializados como JSON antes de ser passado para plotly.js