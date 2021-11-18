import plotly.graph_objects as go # chama o módulo como go para a biblioteca 

fig = go.Figure(go.Scattergeo()) # Cria a fígura e chama o modo geográfico 
# Configuração do mapa
fig.update_geos(
    visible=False, resolution=50, scope="south america", # Visibilidade do mapa desativada, resolução em pixels e o escopo (local)
    showcountries=True, countrycolor="Black", # Exalta o país e a cor ao redor deles
    showsubunits=True, subunitcolor="Blue" # Configuração das divisões dos países do continente selecionado
)
fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0}) # configuração de altura e margem

fig.show() # Plota o gráfico