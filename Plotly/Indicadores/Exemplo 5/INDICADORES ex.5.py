import plotly.graph_objects as go

fig = go.Figure(go.Indicator(
    mode = "number+delta", # o tipo de indicador (número + triângulo de variação)
    value = 400, # valor a ser exibido, podendo ser uma variável
    number = {'prefix': "R$ "},
    delta = {'position': "top", 'reference': 320}, # nível do índice máximo da escala (esse valor definirá se houve aumento ou perda do delta)
    domain = {'x': [0, 1], 'y': [0, 1]}))

fig.update_layout(paper_bgcolor = "#808080") # cor de fundo

fig.show()