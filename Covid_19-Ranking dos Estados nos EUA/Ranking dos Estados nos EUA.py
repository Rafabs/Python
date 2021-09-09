import requests # Extrair dados da url .JSON
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import plotly
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import datetime as dt # Auxilia os dados com data/hora

# Coletando dados
url_request = requests.get("https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/Coronavirus_2019_nCoV_Cases/FeatureServer/1/query?where=1%3D1&outFields=*&outSR=4326&f=json")
url_json = url_request.json()
df = pd.DataFrame(url_json['features'])

# Transformando dados
data_list = df['attributes'].tolist()
data = pd.DataFrame(data_list)
data.set_index('OBJECTID')
data = data[['Province_State','Country_Region','Last_Update','Lat','Long_','Confirmed','Recovered','Deaths','Active']]
data.columns = ('State','Country','Last Update','Lat','Long','Confirmed','Recovered','Deaths','Active')
data['State'].fillna(value = '', inplace = True)
data

# Convertendo o tempo atual
def convert_time(t):
    t = int(t)
    return dt.datetime.fromtimestamp(t)
data = data.dropna(subset = ['Last Update'])
data['Last Update'] = data['Last Update']/1000
data['Last Update'] = data['Last Update'].apply(convert_time)
data

# Variável para filtrar os dados dos EUA
topstates_us = data['Country'] == 'US'
topstates_us = data[topstates_us].nlargest(5, 'Confirmed')

fig1 = go.Figure(data = [
    go.Bar(name = 'Active Cases', x = topstates_us['Active'], y = topstates_us['State'], orientation = 'h'),
    go.Bar(name = 'Death Cases', x = topstates_us['Deaths'], y = topstates_us['State'], orientation = 'h')])
fig1.update_layout(title = 'Ranking dos Estados nos Estados Unidos', height = 600)
fig1.show() # Plota os dados

# go.bar = Gráfico de barras
# color_continuous_scale = escala de cor para os dados,  consultada em: https://plotly.com/python/builtin-colorscales/
## Cada go.Bar é um dado diferente a ser plotado em um único gráfico.

# Fonte: https://medium.com/codex/covid-19-analysis-with-python-b898181ea627