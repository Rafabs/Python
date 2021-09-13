import plotly.graph_objects as px # Biblioteca usada para criar gráficos
import pandas as pd

data = pd.read_csv("tips.csv")
plot = px.Figure(data=[px.Scatter(
    x=data['day'],
    y=data['tip'],
    mode='markers',)
])
plot.update_layout( # Cria o Menu
    updatemenus=[
        dict(
            type="buttons",
            direction="left",
            buttons=list([
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
        ),
    ]
)
plot.show() # Plota o gráfico

# plotly.express pode criar toda a fígura de uma só vez. Ele usa a graph_objects internamente
# long-form data é adequado para armazenar e exibir dados multivariados, ou seja, com dimensões superiores a 2.
