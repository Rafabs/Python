import plotly.graph_objects as go

fig = go.Figure(go.Indicator(
    mode = "number+delta", # o tipo de indicador (número + triângulo de variação)
    value = 492, # valor a ser exibido, podendo ser uma variável
    delta = {"reference": 512, "valueformat": ".0f"}, # nível do índice máximo da escala (esse valor definirá se houve aumento ou perda do delta)
    title = {"text": "Usuários online"}, # título do gráfico
    domain = {'y': [0, 1], 'x': [0.25, 0.75]}))

fig.add_trace(go.Scatter( # gráfico scatter
    y = [325, 324, 405, 400, 424, 404, 417, 432, 419, 394, 410, 426, 413, 419, 404, 408, 401, 377, 368, 361, 356, 359, 375, 397, 394, 418, 437, 450, 430, 442, 424, 443, 420, 418, 423, 423, 426, 440, 437, 436, 447, 460, 478, 472, 450, 456, 436, 418, 429, 412, 429, 442, 464, 447, 434, 457, 474, 480, 499, 497, 480, 502, 512, 492]))

fig.update_layout(xaxis = {'range': [0, 62]}) # Eixo X de 0 à 62
fig.show()