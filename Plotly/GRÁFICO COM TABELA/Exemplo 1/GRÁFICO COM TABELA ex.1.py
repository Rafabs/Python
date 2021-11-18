import plotly.graph_objects as go 
fig = go.Figure(data=[go.Table(header=dict(values=['A Scores', 'B Scores']), # Cria a tabela com cabeçalho de 2 colunas
                 cells=dict(values=[[100, 90, 80, 90], [95, 85, 75, 95]])) # Os valores apresentados,colunas separadas por [],[]...
                     ])

import plotly.graph_objects as go # Biblioteca usada para criar gráficos
from plotly.subplots import make_subplots # Biblioteca usada para criar gráficos com subplots
import pandas as pd # Biblioteca usada para criar dataframes
import re # Regular Expression operations

# Cria o dataframe com os dados 'puxados'
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/Mining-BTC-180.csv")  

for i, row in enumerate(df["Date"]):
    p = re.compile(" 00:00:00")
    datetime = p.split(df["Date"][i])[0]
    df.iloc[i, 1] = datetime

# Cria a janela com os dados (1 tabela, 2 gráficos)
fig = make_subplots(
    rows=3, cols=1,
    shared_xaxes=True,
    vertical_spacing=0.03,
    specs=[[{"type": "table"}],
           [{"type": "scatter"}],
           [{"type": "scatter"}]]
)

# Cria o gráfico
fig.add_trace(
    go.Scatter(
        x=df["Date"], # Dados o eixo X
        y=df["Mining-revenue-USD"], # Dados o eixo Y
        mode="lines", 
        name="mining revenue"
    ),
    row=3, col=1
)

# Cria o gráfico
fig.add_trace(
    go.Scatter(
        x=df["Date"], # Dados o eixo X
        y=df["Hash-rate"], # Dados o eixo Y
        mode="lines",
        name="hash-rate-TH/s"
    ),
    row=2, col=1
)

# Cria a tabela
fig.add_trace(
    go.Table(
        # Informações do cabeçalho
        header=dict(
            values=["Date", "Number<br>Transactions", "Output<br>Volume (BTC)",
                    "Market<br>Price", "Hash<br>Rate", "Cost per<br>trans-USD",
                    "Mining<br>Revenue-USD", "Trasaction<br>fees-BTC"],
            font=dict(size=10),
            align="left"
        ),
        # Informações das células
        cells=dict(
            values=[df[k].tolist() for k in df.columns[1:]],
            align = "left")
    ),
    row=1, col=1
)

# Configurações do layout
fig.update_layout(
    height=800,
    showlegend=False,
    title_text="Bitcoin mining stats for 180 days",
)

fig.show() # Plota o gráfico
