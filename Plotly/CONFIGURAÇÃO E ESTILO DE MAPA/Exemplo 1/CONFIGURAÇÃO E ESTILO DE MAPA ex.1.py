import plotly.graph_objects as go # chama o módulo como go para a biblioteca 

fig = go.Figure(go.Scattergeo()) # Cria a fígura e chama o modo geográfico
fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0}) # configuração de altura e margem

fig.show() # Plota o gráfico