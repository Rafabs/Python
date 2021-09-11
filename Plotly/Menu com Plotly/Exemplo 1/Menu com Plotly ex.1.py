import plotly.graph_objects as px # Biblioteca usada para criar gráficos
import numpy as np

np.random.seed(42)
random_x = np.random.randint(1, 101, 100) # Valores do eixo X
random_y = np.random.randint(1, 101, 100) # Valores do eixo Y
plot = px.Figure(data=[px.Scatter(
    x=random_x,
    y=random_y,
    mode='markers',)
])
plot.update_layout( # Cria o Menu
    updatemenus=[
        dict(
            buttons=list([ # Lista dos botões
                dict( # Botão 1 - Scatter Plot
                    args=["type", "scatter"],
                    label="Scatter Plot",
                    method="restyle"
                ),
                dict( # Botão 2 - Bar Chart
                    args=["type", "bar"],
                    label="Bar Chart",
                    method="restyle"
                )
            ]),
            direction="down",
        ),
    ]
)
plot.show() # Plota o gráfico

# plotly.express pode criar toda a fígura de uma só vez. Ele usa a graph_objects internamente
# long-form data é adequado para armazenar e exibir dados multivariados, ou seja, com dimensões superiores a 2.