Mapas de bolhas em Python

Como fazer mapas de bolhas em Python com Plotly.

Configuração do mapa base
Figuras parcelas feitas com Expresso Plotly px.scatter_geo, ou funções ou contendo ou 
px.line_geopx.choroplethgo.Choroplethgo.Scattergeo objetos gráficos ter um objeto que pode ser usado 
para go.layout.Geocontrolar a aparência do mapa base sobre quais dados são plotados.

Mapa de bolhas com Plotly Express
Expresso Plotly é a interface de alto nível e fácil de usar para Plotly, que opera em uma variedade de 
tipos de dados e produz figuras fáceis de estilo. Com , cada linha do dataframe é representada como um 
ponto marcador. A coluna definida como o argumento dá o tamanho dos marcadores.px.scatter_geosize


Mapa de bolhas com go.Scattergeo
Mapa da Bolha dos Estados Unidos

Para dimensionar o tamanho da bolha, use o sizeref de atributo. Recomendamos usar a seguinte fórmula 
para calcular um valor sizeref:

sizeref = 2. * max(array of size values) / (desired maximum marker size ** 2)

Observe que a configuração para um valor superior a US $ 1$, diminui os tamanhos de marcador 
renderizados, enquanto a configuração para menos de US $ 1$, aumenta os tamanhos de marcadores 
sizes.sizerefsizeref

