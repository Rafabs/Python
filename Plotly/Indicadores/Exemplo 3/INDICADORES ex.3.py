import plotly.graph_objects as go

fig = go.Figure(go.Indicator(
    mode = "number+gauge+delta", # o tipo de indicador (medida + número + triângulo de variação)
    gauge = {'shape': "bullet"}, # configurando o tipo do medidor: barra em escala
    delta = {'reference': 300}, # nível do índice máximo da escala (esse valor definirá se houve aumento ou perda do delta)
    value = 220, # valor a ser exibido, podendo ser uma variável
    domain = {'x': [0.1, 1], 'y': [0.2, 0.9]},
    title = {'text': "Avg order size"})) # título do gráfico

fig.show()