import plotly.graph_objects as go # Biblioteca usada para criar gráficos

# Configuração dos dados nas colunas, separadas por [],[],[],...
values = [['Salaries', 'Office', 'Merchandise', 'Legal', '<b>TOTAL<br>EXPENSES</b>'], #1° col.
  ["Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
  "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
  "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
  "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
  "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad"]]

# Cria a tabela
fig = go.Figure(data=[go.Table(
  columnorder = [1,2], # Ordem das colunas
  columnwidth = [80,400], # Largura das colunas

  # Configuração do cabeçalho
  header = dict(
    values = [['<b>EXPENSES</b><br>as of July 2017'], # <br> utilizado para quebra de linha na mesma célula
                  ['<b>DESCRIPTION</b>']],
    line_color='darkslategray', # Configuração da cor de linha
    fill_color='royalblue', # Configuração da cor de preenchimento
    align=['left','center'], # Posiciona o texto
    font=dict(color='white', size=12), # Cor e tamanho do texto 
    height=40 # Altura das células
  ),

  # Configuração das células
  cells=dict(
    values=values, # Os valores serão os mesmos da variável
    line_color='darkslategray', # Configuração da cor de linha
    fill=dict(color=['paleturquoise', 'white']), # Configuração da cor de preenchimento
    align=['left', 'center'], # Posiciona o texto
    font_size=12, # Tamanho do texto 
    height=30) # Altura das células
    ) 
])

fig.show() # Plota o gráfico

# plotly.express pode criar toda a fígura de uma só vez. Ele usa a graph_objects internamente
