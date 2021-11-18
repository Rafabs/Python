import plotly.graph_objects as go # chama o módulo como go para a biblioteca 

fig = go.Figure(go.Scattergeo()) # Cria a fígura e chama o modo geográfico 
# Configuração do mapa
fig.update_geos(
    visible=False, resolution=110, scope="usa", # Visibilidade do mapa desativada, resolução em pixels e o escopo (local)
    showcountries=True, countrycolor="Black", # Exalta o país e a cor ao redor deles
    showsubunits=True, subunitcolor="Blue" # Configuração das divisões dos países do continente selecionado
)
fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0}) # configuração de altura e margem

fig.show() # Plota o gráfico

'''O escopo contém limites estaduais em ambas as resoluções, e usa a projeção especial que move o Alasca e o Havaí mais perto dos 
"48 estados inferiores" para reduzir a distorção da projeção e produzir um mapa mais compacto."usa"'albers usa'''