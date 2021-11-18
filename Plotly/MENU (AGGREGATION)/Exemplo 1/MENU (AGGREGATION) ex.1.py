import plotly.io as pio

subject = ['Moe','Larry','Curly','Moe','Larry','Curly','Moe','Larry','Curly','Moe','Larry','Curly'] # Variável de nomes para o eixo X
score = [1,6,2,8,2,9,4,5,1,5,2,8] # Variável de nomes para o eixo Y

# Cria o conjunto de dados
data = [dict(
  type = 'scatter', # Tipo dispersão 'scatter'
  x = subject, # Dados do Eixo X
  y = score, # Dados do Eixo Y
  mode = 'markers', # O modo do gráfico
  # Configuração de agregar os dados 
  transforms = [dict(
    type = 'aggregate', # A função 'aggregate' em tipo deve estar ativada
    groups = subject, # A forma de agrupamento
    aggregations = [dict(
        target = 'y', func = 'sum', enabled = True), # Soma os dados que são iguais aos mencionados no eixo X
    ]
  )]
)]

fig_dict = dict(data=data) # Cria a fígura

pio.show(fig_dict, validate=False) # Plota o gráfico