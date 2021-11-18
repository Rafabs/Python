import plotly.graph_objects as go # Biblioteca usada para criar gráficos

fig = go.Figure(data=[go.Table( # Cria a tabela com cabeçalho de 2 colunas
    # Configuração do cabeçalho
    header=dict(values=['A Scores', 'B Scores'],
                line_color='darkslategray', # Configuração da cor de linha
                fill_color='lightskyblue', # Configuração da cor de preenchimento
                align='left'), # Posiciona o texto
                
    # Configuração das células
    cells=dict(values=[[100, 90, 80, 90], # 1° coluna
                       [95, 85, 75, 95]], # 2° coluna
               line_color='darkslategray', # Configuração da cor de linha
               fill_color='lightcyan', # Configuração da cor de preenchimento
               align='left'))# Posiciona o texto
])

fig.update_layout(width=500, height=300) # Tamanho do layout (tabela)

fig.show() # Plota o gráfico

