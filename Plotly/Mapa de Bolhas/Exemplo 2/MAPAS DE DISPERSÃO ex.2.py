# Mapa de bolhas com Plotly Express ANIMADO

import plotly.express as px # chama o módulo como px para a biblioteca 

df = px.data.gapminder() # Cria o dataframe com dados do arquivo gapminder (padrão do Plotly)

fig = px.scatter_geo(df, locations="iso_alpha", color="continent", # A cor é diferenciada pela coluna "continent" 
                     hover_name="country", size="pop", # Tamanho do marcador, "pop" é uma das colunas do arquivo gapminder
                     animation_frame="year", # A animação é dada por esse comando, que faz frame a frame com base na coluna "year"                     
                     projection="natural earth") # A projeção é dada pela coluna "natural earth"
fig.show() # Plota o gráfico