# Mapa de bolhas com Plotly Express

import plotly.express as px # chama o módulo como px para a biblioteca 

df = px.data.gapminder().query("year==2007") # Cria o dataframe com dados do arquivo gapminder (padrão do Plotly)

fig = px.scatter_geo(df, locations="iso_alpha", color="continent", # A cor é diferenciada pela coluna "continent" 
                     hover_name="country", size="pop", # Tamanho do marcador, "pop" é uma das colunas do arquivo gapminder
                     projection="natural earth") # A projeção é dada pela coluna "natural earth"
fig.show() # Plota o gráfico