import plotly.express as px # chama o módulo como px para a biblioteca 

fig = px.line_geo(lat=[0,15,20,35], lon=[5,10,25,30]) # Cria a fígura e chama o modo geográfico nas coordenadas
# Configuração do mapa
fig.update_geos(fitbounds="locations") # A função fitbounds serve para traçar o mapa
fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0}) # configuração de altura e margem

fig.show() # Plota o gráfico