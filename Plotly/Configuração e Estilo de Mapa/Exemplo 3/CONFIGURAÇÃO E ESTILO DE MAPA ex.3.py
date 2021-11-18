import plotly.graph_objects as go # chama o módulo como go para a biblioteca 

fig = go.Figure(go.Scattergeo()) # Cria a fígura e chama o modo geográfico
# Configuração do mapa
fig.update_geos(
    visible=False, # Desativa a visibilidade de todos os itens, exceto os que estiverem configurados abaixo:
    resolution=50, # Resolução em px (pixel)
    showlakes=True, lakecolor="Blue", # Cor dos lagos
    showrivers=True, rivercolor="Blue" # Cor dos Rios
)
fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0}) # configuração de altura e margem

fig.show() # Plota o gráfico