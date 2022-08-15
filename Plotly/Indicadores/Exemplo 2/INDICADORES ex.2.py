import plotly.graph_objects as go

fig = go.Figure(go.Indicator(
    mode = "gauge+number", # o tipo de indicador (medida + número)
    value = 450, # valor a ser exibido, podendo ser uma variável
    title = {'text': "Velocidade"}, # título do gráfico
    domain = {'x': [0, 1], 'y': [0, 1]} 
))

fig.show()