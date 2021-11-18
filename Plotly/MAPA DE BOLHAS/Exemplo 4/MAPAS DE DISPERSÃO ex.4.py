import plotly.graph_objects as go # chama o módulo como go para a biblioteca 
import pandas as pd # Biblioteca utilizada para criar dataframes 

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_ebola.csv') # Cria o dataframe com dados do arquivo 'linkado'
df.head() # usa o dataframe como cabeçalho

colors = ['rgb(239,243,255)','rgb(189,215,231)','rgb(107,174,214)','rgb(33,113,181)'] # Variável para configuração de cores
months = {6:'June',7:'July',8:'Aug',9:'Sept'}  # Variável para configuração dos meses

# Cria a figura
fig = go.Figure()
for i in range(6,10)[::-1]: # Condição for para cálculo 
    df_month = df.query('Month == %d' %i) # Cria um dataframe para os meses 
    
    # Adiciona alguns dados ao mapa
    fig.add_trace(go.Scattergeo(
            lon = df_month['Lon'], # variável que utiliza os dados de longitude da variável de ajuste do dataframe
            lat = df_month['Lat'], # variável que utiliza os dados de latitude da variável de ajuste do dataframe
            text = df_month['Value'], # variável que utiliza os dados de texto da variável de ajuste do dataframe
            name = months[i], # O nome dos traços são os dados da variável months ajustados pela variável do dado i
            
            # Configuração de marcadores
            marker = dict(
                size = df_month['Value']/50, # o tamanho dos dados da variável do dataframe é proporcional ao df_sub dividido por 50.
                color = colors[i-6], # as cores são proporcionais a variável colors com base no valor de i
                line_width = 0  # a espessura da linha
            )))

# Configuração do dataframe para o mês de Setembro (Ao qual será mostrado no mapa)
df_sept = df.query('Month == 9') 
fig['data'][0].update(mode='markers+text', textposition='bottom center', # Cria a figura com os dados e adiciona um modo de marcador com texto, o texto do marcador centralizado
                      text=df_sept['Value'].map('{:.0f}'.format).astype(str)+' '+ df_sept['Country']) # O texto será o valor do dataframe criado seguido do dado da coluna 'Country'

# Adiciona mais dados a figura (Choropleth = Mapa coroplético)
fig.add_trace(go.Choropleth(
        locationmode = 'country names', # O modo dos locais 
        locations = df_sept['Country'], # A localização é dada pela variável do dataframe criado 
        z = df_sept['Value'], # Cria a variável para inserção do valor do dataframe criado
        text = df_sept['Country'], # Cria a variável para inserção do texto do dataframe criado
        colorscale = [[0,'rgb(0, 0, 0)'],[1,'rgb(0, 0, 0)']], # Config. de escala de cor
        autocolorscale = False, # Desativa a escala de cor automática
        showscale = False, # Desativa a escala 
        geo = 'geo2' 
    ))

# Adiciona mais dados a figura (A serem exibidas quando o cursor do mouse passar sobre ele)
fig.add_trace(go.Scattergeo(
        lon = [21.0936], # Variável de longitude do mapa exibido
        lat = [7.1881], # Variável de latitude do mapa exibido
        text = ['Africa'], # Exibe o texto do país 
        mode = 'text', # o modo do mapa
        showlegend = False, # Desativa a legenda
        geo = 'geo2'
    ))

# Adiciona mais dados a figura (TÍTULO)
fig.update_layout(
    # Cria o título 
    title = go.layout.Title(
        text = 'Ebola cases reported by month in West Africa 2014<br> \
Source: <a href="https://data.hdx.rwlabs.org/dataset/rowca-ebola-cases">\
HDX</a>'), # Texto com hiperlink
    
    # Cria o mapa geográfico 1
    geo = go.layout.Geo(
        resolution = 50, # resolução do mapa
        scope = 'africa', # O país a ser exibido
        showframe = False, # Desativa a animação de quadros 
        showcoastlines = True, # Ativa as linhas das ilhas próximas
        landcolor = "rgb(229, 229, 229)", # Configuração de cor
        countrycolor = "white" , # Cor do país
        coastlinecolor = "white", # Cor das ilhas próximas
        projection_type = 'mercator', # Tipo de projeção 
        # Posição de lat/long do mapa plotado
        lonaxis_range= [ -15.0, -5.0 ], 
        lataxis_range= [ 0.0, 12.0 ],
        domain = dict(x = [ 0, 1 ], y = [ 0, 1 ])
    ),
    
    # Cria o mapa geográfico 2
    geo2 = go.layout.Geo(
        scope = 'africa', # O país a ser exibido
        showframe = False, # Desativa a animação de quadros 
        landcolor = "rgb(229, 229, 229)", # Configuração de cor
        showcountries = False, # Desativa a exibição dos demais países
        domain = dict(x = [ 0, 0.6 ], y = [ 0, 0.6 ]),
        bgcolor = 'rgba(255, 255, 255, 0.0)', # Configuração de cor de fundo
    ),
    legend_traceorder = 'reversed' 
)

fig.show() # Plota o gráfico