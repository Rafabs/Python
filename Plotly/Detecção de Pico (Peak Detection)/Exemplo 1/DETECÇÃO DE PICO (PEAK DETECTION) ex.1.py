import plotly.graph_objects as go # Biblioteca usada para criar gráficos
import pandas as pd # Biblioteca usada para criar dataframe
from scipy.signal import find_peaks # Biblioteca usada para identificar picos 

# Variáveis para 'puxar' os dados
milk_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/monthly-milk-production-pounds.csv')
time_series = milk_data['Monthly milk production (pounds per cow)']

indices = find_peaks(time_series)[0]

# Cria o gráfico de dispersão
fig = go.Figure()
fig.add_trace(go.Scatter(
    y=time_series,
    mode='lines+markers',
    name='Original Plot'
))

# Adiciona a dispersão (scatter)
fig.add_trace(go.Scatter(
    x=indices,
    y=[time_series[j] for j in indices],
    mode='markers',
    marker=dict(
        size=8,
        color='red',
        symbol='cross'
    ),
    name='Detected Peaks'
))

fig.show() # Plota o gráfico

# plotly.express pode criar toda a fígura de uma só vez. Ele usa a graph_objects internamente