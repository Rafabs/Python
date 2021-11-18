# Peronalizando o mapa de dispersão (scatter)

import plotly.express as px # chama o módulo como px para a biblioteca 

df = px.data.gapminder().query("year == 2007") # Cria o dataframe com dados do arquivo gapminder (padrão do Plotly)
fig = px.scatter_geo(df, locations="iso_alpha",
                     color="continent", # As cores utilizadas serão utilizadas pela coluna "continent"
                     hover_name="country", # Usa a coluna "country" como título do assunto
                     size="pop", # Tamanho do marcador, "pop" é uma das colunas do arquivo gapminder
                     projection="natural earth") # projection eem geo é o tipo de mapa escolhido
fig.show() # Plota o gráfico