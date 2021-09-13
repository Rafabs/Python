import plotly.graph_objects as px # Biblioteca usada para criar gráficos
import plotly.express as go
import numpy as np

df = go.data.tips()
x = df['total_bill']
y = df['day']
plot = px.Figure(data=[px.Scatter(
    x=x,
    y=y,
    mode='lines',)
])
plot.update_layout( # Criando controles deslizantes
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                    step="day",
                    stepmode="backward"),
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
    )
)
plot.show() # Plota o gráfico

# plotly.express pode criar toda a fígura de uma só vez. Ele usa a graph_objects internamente
# long-form data é adequado para armazenar e exibir dados multivariados, ou seja, com dimensões superiores a 2.
