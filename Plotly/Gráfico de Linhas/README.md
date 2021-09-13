# Gráfico de Linhas 
O plot de linha em Plotly é uma anexação muito acessível e ilustre ao plotly que gerencia uma variedade de tipos de dados e monta estatísticas fáceis de estilo. Com *px.line* cada posição de dados é representada como um vértice (que a localização é dada pelas colunas x e y) de uma marca de poliline no espaço 2D.
Em uma trama de linha 2D, cada linha de é representada como vértice de uma marca de polilina no espaço 2D.data_frame

plotly.express.line(data_frame=None, x=None, y=None, line_group=None, color=None, line_dash=None, symbol=None, hover_name=None, hover_data=None, custom_data=None, text=None, facet_row=None, facet_col=None, facet_col_wrap=0, facet_row_spacing=None, facet_col_spacing=None, error_x=None, error_x_minus=None, error_y=None, error_y_minus=None, animation_frame=None, animation_group=None, category_orders=None, labels=None, orientation=None, color_discrete_sequence=None, color_discrete_map=None, line_dash_sequence=None, line_dash_map=None, symbol_sequence=None, symbol_map=None, markers=False, log_x=False, log_y=False, range_x=None, range_y=None, line_shape=None, render_mode='auto', title=None, template=None, width=None, height=None)

# data_frame 
(DataFrame ou array-like ou dict) – Este argumento precisa ser passado para que nomes de coluna (e não nomes de palavras-chave) sejam usados. O array-like e o dict são tranformados internamente para um DataFrame pandas. Opcional: se faltar, um DataFrame é construído sob o capô usando os outros argumentos.
# x 
(str ou int ou série ou array-like) – Ou um nome de uma coluna em , ou uma série de pandas ou array_like objeto. Valores desta coluna ou array_like são usados para posicionar marcas ao longo do eixo x em coordenadas cartesianas. Ou pode, opcionalmente, ser uma lista de referências de coluna ou array_likes, nesse caso os dados serão tratados como se fossem "largos" em vez de "longos".data_framexy
# y 
(str ou int ou série ou array-like) – Ou um nome de uma coluna em , ou uma série de pandas ou array_like objeto. Os valores desta coluna ou array_like são usados para posicionar marcas ao longo do eixo y em coordenadas cartesianas. Ou pode, opcionalmente, ser uma lista de referências de coluna ou array_likes, nesse caso os dados serão tratados como se fossem "largos" em vez de "longos".data_framexy
# line_group 
(str ou int ou série ou array-like) – Ou um nome de uma coluna em , ou uma série de pandas ou array_like objeto. Os valores desta coluna ou array_like são usados para agrupar linhas de linhas.data_framedata_frame
# color 
(str ou int ou série ou array-like) – Ou um nome de uma coluna em , ou uma série pandas ou array_like objeto. Os valores desta coluna ou array_like são usados para atribuir cor às marcas.data_frame
# line_dash 
(str ou int ou série ou array-like) – Ou um nome de uma coluna em , ou uma série de pandas ou array_like objeto. Valores desta coluna ou array_like são usados para atribuir padrões de traço a linhas.data_frame
# symbol 
(str ou int ou série ou array-like) – Ou um nome de uma coluna em , ou uma série de pandas ou array_like objeto. Valores desta coluna ou array_like são usados para atribuir símbolos a marcas.data_frame
# hover_name 
(str ou int ou série ou array-like) – Ou um nome de uma coluna em , ou uma série de pandas ou array_like objeto. Valores desta coluna ou array_like aparecem em negrito na ponta da ferramenta hover.data_frame
# hover_data 
(lista de str ou int,ou Série ou array-like,ou dict) – Ou uma lista de nomes de colunas em , ou pandas Series, ou array_like objetos ou um dict com nomes de coluna como teclas, com valores Verdadeiro (para formatação padrão) Falso (a fim de remover esta coluna de informações hover), ou uma sequência de formatação, por exemplo ':.3f' ou '| %a' ou dados semelhantes a listas para aparecer na ponta de ferramenta de hover ou tuplas com uma sequência de bool ou formatação como primeiro elemento, e dados semelhantes a listas para aparecer em pairar como segundo elemento Os valores dessas colunas aparecem como dados extras na ponta da ferramenta hover.data_frame
# custom_data 
(lista de str ou int,ou série ou array-like) – Ou nomes de colunas em , ou pandas Series, ou objetos de array_like Os valores dessas colunas são dados extras, para serem usados em widgets ou retornos de chamada dash, por exemplo. Esses dados não são visíveis pelo usuário, mas estão incluídos em eventos emitidos pela figura (seleção de laços etc.)data_frame
# text  
(str ou int ou série ou array-like) – Ou um nome de uma coluna em , ou uma série pandas ou array_like objeto. Valores desta coluna ou array_like aparecem na figura como rótulos de texto.data_frame
# facet_row 
(str ou int ou série ou array-like) – Ou um nome de uma coluna em , ou uma série de pandas ou array_like objeto. Os valores desta coluna ou array_like são usados para atribuir marcas a subtramas facetizadas na direção vertical.data_frame
# facet_col 
(str ou int ou série ou array-like) – Ou um nome de uma coluna em , ou uma série de pandas ou array_like objeto. Os valores desta coluna ou array_like são usados para atribuir marcas a subtramas facetted na direção horizontal.data_frame
# facet_col_wrap 
(int)– Número máximo de colunas de facetas. Enrola a variável coluna nesta largura, de modo que as facetas da coluna abrangem várias linhas. Ignorado se 0, e forçado a 0 se ou um é definido.facet_rowmarginal
# facet_row_spacing 
(flutuar entre 0 e 1) – Espaçamento entre linhas de facetas, em unidades de papel. A inadimplência é de 0,03 ou 0,0,7 quando facet_col_wrap é usada.
# facet_col_spacing 
(flutuar entre 0 e 1) – Espaçamento entre colunas de facetas, em unidades de papel O padrão é 0,02.
# error_x 
(str ou int ou série ou array-like) – Ou um nome de uma coluna em , ou uma série de pandas ou array_like objeto. Os valores desta coluna ou array_like são usados para dimensionar barras de erro do eixo x. Se for, as barras de erro serão simétricas, caso contrário, serão usadas apenas para a direção positiva.data_frameerror_x_minusNoneerror_x
# error_x_minus 
(str ou int ou série ou array-like) – Ou um nome de uma coluna em , ou uma série de pandas ou array_like objeto. Os valores desta coluna ou array_like são usados para dimensionar barras de erro do eixo x na direção negativa. Ignorado se é .data_frameerror_xNone
# error_y 
(str ou int ou série ou array-like) – Ou um nome de uma coluna em , ou uma série de pandas ou array_like objeto. Os valores desta coluna ou array_like são usados para dimensionar barras de erro do eixo y. Se for, as barras de erro serão simétricas, caso contrário, serão usadas apenas para a direção positiva.data_frameerror_y_minusNoneerror_y
# error_y_minus
(str ou int ou série ou array-like) – Ou um nome de uma coluna em , ou uma série de pandas ou array_like objeto. Os valores desta coluna ou array_like são usados para dimensionar barras de erro do eixo y na direção negativa. Ignorado se é .data_frameerror_yNone
# animation_frame 
(str ou int ou série ou array-like) – Ou um nome de uma coluna em , ou uma série de pandas ou array_like objeto. Valores desta coluna ou array_like são usados para atribuir marcas a quadros de animação.data_frame
# animation_group 
(str ou int ou série ou array-like) – Ou um nome de uma coluna em , ou uma série de pandas ou array_like objeto. Os valores desta coluna ou array_like são usados para fornecer constância de objetos em todos os quadros de animação: linhas com animation_groupcorrespondentes serão tratadas como se descrevessem o mesmo objeto em cada quadro.data_frame
# category_orders 
(dict com teclas str e lista de valores str (padrão )) – Por padrão, no Python 3.6+, a ordem de valores categóricos em eixos, lendas e facetas depende da ordem em que esses valores são encontrados pela primeira vez (e nenhuma ordem é garantida por padrão no Python abaixo de 3,6). Este parâmetro é usado para forçar uma ordenação específica de valores por coluna. As teclas deste dicto devem corresponder aos nomes das colunas, e os valores devem ser listas de strings correspondentes à ordem de exibição específica desejada.{}data_frame
# labels  
(dict com teclas str e valores str (padrão )) – Por padrão, os nomes das colunas são usados na figura para títulos de eixo, entradas de legendas e pairar. Este parâmetro permite que este seja substituído. As teclas deste dicto devem corresponder aos nomes das colunas, e os valores devem corresponder à etiqueta desejada a ser exibida.{}
# orientation  
(str, uma para horizontal ou para vertical.) – (padrão se e são fornecidos e ambos continuosos ou ambos categóricos, caso contrário 'h') é categórico e ) é contínuo, caso contrário 'h') é fornecido)'h''v''v'xy'v'`() if `x`(`yy`(`x'v'`() if only `x`(`y
# color_discrete_sequence 
(lista de str) – As cordas devem definir cores CSS válidas. Quando é definido e os valores na coluna correspondente não são numéricos, os valores nessa coluna são atribuídos cores por ciclo através da ordem descrita em , a menos que o valor de seja uma chave em . Várias sequências de cores úteis estão disponíveis nos submodules, especificamente .colorcolor_discrete_sequencecategory_orderscolorcolor_discrete_mapplotly.express.colorsplotly.express.colors.qualitative
# color_discrete_map
(dict com teclas str e valores str (padrão )) – Os valores de string devem definir cores CSS válidas Usados para substituir para atribuir uma cor específica a marcas correspondentes com valores específicos. As teclas devem ser valores na coluna denotadas por . Alternativamente, se os valores de cores válidas, a sequência pode ser passada para fazê-las ser usadas diretamente.{}color_discrete_sequencecolor_discrete_mapcolorcolor'identity'
# line_dash_sequence 
(lista de str) – As cordas devem definir os padrões de traço válidos.js. Quando é definido, os valores nessa coluna são atribuídos padrões de traço através do ciclo através da ordem descrita em , a menos que o valor de é uma chave em .line_dashline_dash_sequencecategory_ordersline_dashline_dash_map
# line_dash_map 
(dict com teclas str e valores str (padrão )) – Os valores de strings definem plotly.js dash-patterns. Usado para substituir para atribuir um traço específico a linhas correspondentes a valores específicos. As teclas devem ser valores na coluna denotadas por . Alternativamente, se os valores de são nomes válidos de traço de linha, a sequência pode ser passada para fazê-los serem usados diretamente.{}line_dash_sequencesline_dash_mapline_dashline_dash'identity'
# symbol_sequence 
(lista de str) – As cordas devem definir símbolos .js valido. Quando definidos, os valores nessa coluna são atribuídos símbolos por ciclismo através da ordem descrita em , a menos que o valor de é uma chave em .symbolsymbol_sequencecategory_orderssymbolsymbol_map
# symbol_map 
(dict com teclas str e valores str (padrão )) – Os valores de string devem definir plotly.js símbolos Usados para substituir para atribuir um símbolo específico a marcas correspondentes com valores específicos. As teclas devem ser valores na coluna denotadas por . Alternativamente, se os valores de são nomes de símbolos válidos, a sequência pode ser passada para fazê-los ser usados diretamente.{}symbol_sequencesymbol_mapsymbolsymbol'identity'
# marcadores 
(boolean (default )) – Se , marcadores são mostrados em linhas.FalseTrue
# log_x 
(boolean (default  )) – Se , o eixo x é dimensionado em coordenadas cartesianas.FalseTrue
# log_y 
(boolean (default  )) – Se , o eixo y é dimensionado em coordenadas cartesianas.FalseTrue
# range_x 
(lista de dois números) – Se fornecido, substitui o auto-dimensionamento no eixo x em coordenadas cartesianas.
# range_y 
(lista de dois números) – Se fornecido, substitui o auto-dimensionamento no eixo y em coordenadas cartesianas.
# line_shape 
(str (default  )) – Um de ou .'linear''linear''spline'
# render_mode 
(str) – Um dos , ou , padrão Controla a API do navegador usada para desenhar marcas. ' é apropriado para números inferiores a 1000 pontos de dados, e permitirá uma saída totalmente vetorializada. é provável que seja necessário para um desempenho aceitável acima de 1000 pontos, mas rasteriza parte da saída. usa heurística para escolher o modo.'auto''svg''webgl''auto''svg'webgl''auto'
# title 
(str) O título da figura.
# template  
(str ou dict ou plotly.graph_objects.layout.Exemplo de exemplo) – O nome do modelo de figura (deve ser uma chave em plotly.io.templates) ou definição.
# width  
(int (default  )) – A largura da figura em pixels.None
# height 
(int (default  )) – A altura da figura em pixels.None

Fonte: https://plotly.com/python-api-reference/generated/plotly.express.line
