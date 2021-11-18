import plotly.graph_objects as go # chama o módulo como go para a biblioteca 
import pandas as pd # Biblioteca utilizada para criar dataframes 

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_us_cities.csv') # Cria o dataframe com dados do arquivo 'linkado'
df.head() # usa o dataframe como cabeçalho

df['text'] = df['name'] + '<br>Population ' + (df['pop']/1e6).astype(str)+' million' # o texto é dado pelo nome = quantidade da população / 1e6 em milhões
limits = [(0,2),(3,10),(11,20),(21,50),(50,3000)] # variável para criar a legenda lateral
colors = ["royalblue","crimson","lightseagreen","orange","lightgrey"] # variável para criar as cores da legenda lateral
cities = [] # variável para criar uma lista de cidades
scale = 5000 # variável para escala do mapa

# Cria a figura
fig = go.Figure()

for i in range(len(limits)): # Condição for para cálculo 
    lim = limits[i] # variável para ajustar a variável limits com dados do valor i
    df_sub = df[lim[0]:lim[1]] # variável para ajuste do dataframe
    fig.add_trace(go.Scattergeo( # adiciona a subfigura na figura
        locationmode = 'USA-states', # usa os dados dos estados dos EUA
        lon = df_sub['lon'], # variável que utiliza os dados de longitude da variável de ajuste do dataframe
        lat = df_sub['lat'], # variável que utiliza os dados de latitude da variável de ajuste do dataframe
        text = df_sub['text'], # variável que utiliza os dados de texto da variável de ajuste do dataframe
        
        # Configuração de marcadores
        marker = dict(
            size = df_sub['pop']/scale, # o tamanho dos dados da coluna população é proporcional ao df_sub dividido pela variável de escala
            color = colors[i], # as cores são proporcionais a variável colors com base no valor de i
            line_color='rgb(40,40,40)', # as cores de linhas RGB
            line_width=0.5, # a espessura da linha
            sizemode = 'area' # o modo 
        ),
        name = '{0} - {1}'.format(lim[0],lim[1])))

# Adiciona mais dados a figura
fig.update_layout(
        title_text = '2014 US city populations<br>(Click legend to toggle traces)', # Nome do gráfico (título)
        showlegend = True, # Ativa a legenda
        # Configuração de dados geográficos
        geo = dict(
            scope = 'usa', # Utiliza o mapa dos EUA
            landcolor = 'rgb(217, 217, 217)', # Configuração das cores do mapa em questão
        )
    )

fig.show() # Plota o gráfico