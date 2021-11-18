import plotly.express as px # Biblioteca usada para criar gráficos
import plotly.graph_objects as go

df = px.data.tips() # DataFrame com conjunto de dados
fig = go.Figure(data =[go.Scatter3d(x = df['total_bill'],
                                   y = df['time'],
                                   z = df['tip'],
                                   mode ='markers')])  # Cria o objeto com os dados de x e y automaticamente por plotly.
fig.show() # Plota o gráfico

# plotly.express pode criar toda a fígura de uma só vez. Ele usa a graph_objects internamente