Mapas da caixa de mapas vs Mapas Geo
O Plotly suporta dois tipos diferentes de mapas:

Mapas da caixa de mapas são mapas à base de ladrilhos. Se sua figura for criada com uma função ou de 
outra forma contiver um ou mais traços de tipo, ou , o objeto em sua figura contém informações de 
configuração para o próprio 
mapa.px.scatter_mapboxpx.line_mapboxpx.choropleth_mapboxpx.density_mapboxgo.Scattermapboxgo.Choroplethmapboxgo.Densitymapboxlayout.mapbox

Mapas geográficos são mapas baseados em contornos. Se sua figura for criada com uma função ou de outra 
forma contiver um ou mais traços de tipo ou , o objeto em sua figura contém informações de configuração 
para o próprio mapa.px.scatter_geopx.line_geopx.choroplethgo.Scattergeogo.Choroplethlayout.geo
Esta página documenta mapas baseados em contorno geo, e o Documentação de camadas de caixa de mapas 
descreve como configurar mapas baseados em ladrilhos mapbox.

Nota: Plotly Express não pode criar figuras vazias, então os exemplos abaixo criam principalmente um 
mapa "vazio" usando . Dito isto, todas as opções de configuração aqui são igualmente aplicáveis a mapas 
não vazios criados com o Plotly Express , ou 
funções.fig = go.Figure(go.Scattergeo())px.scatter_geopx.line_geopx.choropleth

Mapas da Base Física
Plotly Geo mapeia uma camada de mapa base incorporada composta de dados "físicos" e "culturais" 
(ou seja, fronteira administrativa) do Conjunto de dados da Terra Natural. Várias linhas e 
preenchimentos de área podem ser mostrados ou escondidos, e suas cores e larguras de linha 
especificadas. No modelo padrãoplotly, um quadro de mapas e características físicas, como um contorno 
costeiro e áreas de terra preenchidas são mostrados, em uma resolução de 1:110m em pequena escala.


Projeção de Mapas
Mapas geográficos são desenhados de acordo com um determinado mapa projeção que achata a superfície aproximadamente esférica da Terra em um espaço bidimensional.

As projeções disponíveis são, , , , , ,'equirectangular''mercator''orthographic''natural earth'
'kavrayskiy7''miller''robinson''eckert4''azimuthal equal area''azimuthal equidistant''conic equal area'
'conic conformal''conic equidistant''gnomonic''stereographic''mollweide''hammer''transverse mercator'
'albers usa''winkel tripel''aitoff''sinusoidal'

As projeções do mapa podem ser giradas usando o atributo, e os mapas podem ser traduzidos usando o 
atribuído, bem como truncados a uma certa faixa de longitude e latitude usando o e 
.layout.geo.projection.rotationlayout.geo.centerlayout.geo.lataxis.rangelayout.geo.lonaxis.range

Montagem automática de zoom ou limites
O atributo pode ser definido para definir automaticamente o centro e latitude e faixa de longitude de 
acordo com os dados que estão sendo plotados. Veja o layout.geo.fitboundslocationsmapas de choropleth 
documentação para mais informações.


Denominado Escopos de Mapa e Subsumes de país
Além disso, o chamado "escopo" de um mapa define um subconto da superfície da Terra para desenhar. 
Cada escopo tem um tipo de projeção padrão, centro e rolo, bem como limites,e certos escopos contêm 
camadas culturais sub-unitárias do país certas resoluções, como na qual contém limites do estado dos 
EUA e província canadense.scope="north america"resolution=50

Os escopos disponíveis são: 'world''usa''europe''asia''africa''north america''south america'





