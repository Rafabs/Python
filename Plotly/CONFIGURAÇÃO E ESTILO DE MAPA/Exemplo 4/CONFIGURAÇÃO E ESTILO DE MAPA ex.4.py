import plotly.graph_objects as go # chama o módulo como go para a biblioteca 

fig = go.Figure(go.Scattergeo()) # Cria a fígura e chama o modo geográfico
# Configuração do mapa
fig.update_geos(projection_type="orthographic") # Cria o mapa (globo) e o tipo, ortográfico
fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0}) # configuração de altura e margem

fig.show() # Plota o gráfico

''' Mapas geográficos são desenhados de acordo com um determinado mapa projeção que achata a superfície aproximadamente 
esférica da Terra em um espaço bidimensional. '''