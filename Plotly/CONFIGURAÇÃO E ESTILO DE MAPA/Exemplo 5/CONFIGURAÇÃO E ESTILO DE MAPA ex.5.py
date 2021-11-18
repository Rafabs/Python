import plotly.graph_objects as go # chama o módulo como go para a biblioteca 

fig = go.Figure(go.Scattergeo()) # Cria a fígura e chama o modo geográfico
# Configuração do mapa
fig.update_geos(
    center=dict(lon=-30, lat=-30), # Centraliza o mapa nas coordenadas
    projection_rotation=dict(lon=30, lat=30, roll=30), # Rotaciona o mapa nas coordenadas
    lataxis_range=[-50,20], lonaxis_range=[0, 200] 
)
fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0}) # configuração de altura e margem

fig.show() # Plota o gráfico

''' Mapas geográficos são desenhados de acordo com um determinado mapa projeção que achata a superfície aproximadamente 
esférica da Terra em um espaço bidimensional. '''