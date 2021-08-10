# Gerando Gráficos com Python
# Lab+ Projetos

import matplotlib.pyplot as plt # Biblioteca para criação de gráficos e dados

dias = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] # Eixo X com dados de dias
temperatura = [26,25,27,26,30,31,35,25,24,23,22,21,20,19,18] # Eixo Y com dados de temperatura

plt.plot (dias,temperatura) # Traçar a linha com os dados de dias/temperatura
plt.title("São Paulo, Abril") # Título do Gráfico
plt.xlabel("Dias") # Nome do Eixo X = Dias
plt.ylabel("Temperatura") # Nome do Eixo Y = Temperatura
plt.show() # Gerando o gráfico
