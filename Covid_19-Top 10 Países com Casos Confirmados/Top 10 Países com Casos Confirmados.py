import requests # Extrair dados da url .JSON
import pandas as pd
import plotly.express as px
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

# Top 10 Países com casos confirmados
top10_confirmed = pd.DataFrame(data.groupby('Country')['Confirmed'].sum().nlargest(10).sort_values(ascending = False))
fig1 = px.scater(top10_confirmed, x = top10_confirmed.index, y = 'Confirmed', size = 'Confirmed', size_max = 120,
                color = top10_confirmed.index, title = 'Top 10 Países com casos confirmados')
fig1.show() # Plota os dados

# >>>>>>>>>>>>>>>>>>>>>>>>Síntaxe para criar o dataframe (Linha 29)<<<<<<<<<<<<<<<<<<<<<<<<<
# Nome da função = pd.DataFrame(data.groupby('Dados na Horizontal')['Dados na Vertical'].sum().nlargest(Quantidade) >>
# >> sort_values(ascending = False))
# ONDE:
# pd.DataFrame = DataFrame do tipo Panda
# data = df (Pacote de Dados original de início)
# data.groupby = usado para agrupar os dados, nesse caso ('Country')['Confirmed']
# sum() = calcula a soma, nesse caso ele não calcula nada, porém faz parte da síntaxe
# nlargest(10) = usado para obter os maiores valores de um quadro de dados ou de uma série, nesse caso, os 10 maiores.
# sort_values(ascending = False) = Classifica por uma categoria de filtro

# >>>>>>>>>>>>>>>>>>>>>>>>Síntaxe para criar o gráfico (Linha 31)<<<<<<<<<<<<<<<<<<<<<<<<<
# Nome do Gráfico no código = tipo de gráfico(Nome da Função, eixo x = Nome da Função.index, eixo y = 'Dados', >>
# >> tamanho = 'Dados', tamanho máximo = 120 cor = Nome da Função.index, título = 'Top 10 Países com casos confirmados')
# ONDE:
# px.scater = Gráfico de bolinhas
# x = Dados que estarão no eixo x, nesse caso, os dados top10_confirmed
# y = Dados que estarão no eixo y, nesse caso, os dados 'Confirmed'
# size = tamanho do gráfico
# size_max = tamanho máximo do gráfico
# color = cor do gráfico, caso necessário
# title = título do gráfico, caso necessário

# Fonte: https://medium.com/codex/covid-19-analysis-with-python-b898181ea627