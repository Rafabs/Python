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

# Cria o layout
layout = dict(
  title = '<b>Plotly Aggregations</b><br>use dropdown to change aggregation', # Cria o título
  xaxis = dict(title = 'Subject'), # Cria o título do eixo x
  yaxis = dict(title = 'Score', range = [0,22]), # Cria o título do eixo y
  # Configurações do menu
  updatemenus = [dict(
        x = 0.85, 
        y = 1.15,
        xref = 'paper',
        yref = 'paper',
        yanchor = 'top',
        active = 1,
        showactive = False,
        buttons = agg_func # O botão deverá ter os dados da lista dos filtros
  )]
)

fig_dict = dict(data=data, layout=layout) # Cria a fígura

pio.show(fig_dict, validate=False) # Plota o gráfico