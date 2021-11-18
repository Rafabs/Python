# Mapa de dispersão (scatter) padrão

import plotly.express as px # chama o módulo como px para a biblioteca 

df = px.data.gapminder().query("year == 2007") # Cria o dataframe com dados do arquivo gapminder (padrão do Plotly)
fig = px.scatter_geo(df, locations="iso_alpha",
                     size="pop", # Tamanho do marcador, "pop" é uma das colunas do arquivo gapminder
                     )
fig.show() # Plota o gráfico