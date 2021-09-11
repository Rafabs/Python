Estrutura do pacote de plotly

Existem três módulos principais em Plotly. Eles são:
plotly.plotly
plotly.graph.objects
plotly.tools

- plotly.plotly atua como a interface entre a máquina local e Plotly. Ele contém funções que requerem 
uma resposta do servidor do Plotly.
- plotly.graph_objects módulo contém os objetos (Figura, layout, dados e a definição dos gráficos como 
gráfico de dispersão, gráfico de linha) que são responsáveis pela criação dos plots. A Figura pode ser 
representada como dict ou instâncias de plotly.graph_objects. Figura e estes são serializados como JSON 
antes de ser passado para plotly.js.
- Nota: o módulo plotly.express pode criar toda a Figura de uma só vez. Ele usa a graph_objects 
internamente e devolve o graph_objects.
