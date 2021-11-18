import plotly.graph_objects as go # chama o módulo como go para a biblioteca 

fig = go.Figure(go.Scattergeo()) # Cria a fígura e chama o modo geográfico
# Configuração do mapa
fig.update_geos(
    resolution=50, # Resolução em px (pixel)
    showcoastlines=True, coastlinecolor="RebeccaPurple", # Cor das costas do globo
    showland=True, landcolor="LightGreen", # Cor das Ilhas
    showocean=True, oceancolor="LightBlue", # Cor do Oceano
    showlakes=True, lakecolor="Blue", # Cor dos lagos
    showrivers=True, rivercolor="Blue" # Cor dos Rios
)
fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0}) # configuração de altura e margem

fig.show() # Plota o gráfico