import plotly.graph_objects as go # Biblioteca usada para criar gráficos

headerColor = 'grey'        # Variável para definir a cor do cabeçalho
rowEvenColor = 'lightgrey'  # Variável para definir a cor da linha intercalada [Even]
rowOddColor = 'white'       # Variável para definir a cor da linha intercalada [Odd]

# Cria a tabela
fig = go.Figure(data=[go.Table(
  # Configuração do cabeçalho
  header=dict(
    values=['<b>EXPENSES</b>','<b>Q1</b>','<b>Q2</b>','<b>Q3</b>','<b>Q4</b>'], # <br> utilizado para quebra de linha na mesma célula
    line_color='darkslategray', # Configuração da cor de linha
    fill_color=headerColor, # Configuração da cor de preenchimento = variável declarada
    align=['left','center'], # Posiciona o texto
    font=dict(color='white', size=12) # Cor e tamanho do texto 
  ),
  # Configuração das células
  cells=dict(
    # Configuração dos dados nas colunas, separadas por [],[],[],...
    values=[
      ['Salaries', 'Office', 'Merchandise', 'Legal', '<b>TOTAL</b>'],
      [1200000, 20000, 80000, 2000, 12120000],
      [1300000, 20000, 70000, 2000, 130902000],
      [1300000, 20000, 120000, 2000, 131222000],
      [1400000, 20000, 90000, 2000, 14102000]],
    line_color='darkslategray', # Configuração da cor de linha

    # Lista 2D de cores para linhas alternadas
    fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]*5], # 5 = Quantidade de linhas intercaladas.
    align = ['left', 'center'], # Posiciona o texto
    font = dict(color = 'darkslategray', size = 11) # Cor e tamanho do texto 
    ))
])

fig.show() # Plota o gráfico

# plotly.express pode criar toda a fígura de uma só vez. Ele usa a graph_objects internamente