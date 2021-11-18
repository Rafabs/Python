import plotly.express as px # Biblioteca usada para criar gráficos

df = px.data.tips() # DataFrame com conjunto de dados 
fig = px.bar(df, x="total_bill", y="sex", color='day', orientation='h', # Cria o objeto com os dados de x e y na horizontal
             hover_data=["tip", "size"], # Cria o objeto com os dados de x e y na horizontal
             height=400, # Altura de 400
             title='Restaurant bills') # Altura de 400

fig.show() # Plota o gráfico

# plotly.express pode criar toda a fígura de uma só vez. Ele usa a graph_objects internamente

''' Hover Labels: Um dos recursos mais enganosamente poderosos da visualização interativa usando o Plotly 
é a capacidade do usuário de revelar mais informações sobre um ponto de dados movendo seu cursor do mouse 
sobre o ponto e tendo um rótulo hover aparecendo.
Existem três modos de hover disponíveis no Plotly. A configuração padrão é layout.hovermode='closest', 
onde uma única etiqueta de hover aparece para o ponto diretamente abaixo do cursor.'''