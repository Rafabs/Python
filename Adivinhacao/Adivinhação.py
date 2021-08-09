segredo = 7 #Define o numero secreto
print("Vamos tentar adivinhar o numero secreto")
numero = int(input("Digite seu palpite"))  #Recebe a entrada e transforma em numero
print("Você digitou ", numero) #Apresenta um texto e uma variavel

#Verifica cada uma das possibilidade
if segredo > numero:
    print("O número digitado foi menor que o numero secreto")
elif segredo < numero:
    print("O número digitado foi maior que o numero secreto")
else:
    print("Parabéns! Acertou!")
