from tkinter import *
janela = Tk()
contador = 0 # Definimos o contador, comecando em 0
 
def clicou(): # Cada vez que o botão for pressionado entra nesta funcao
    global contador # Utilizamos uma variavel nao definida dentro da funcao
    contador = contador + 1 # E adicionado 1 ao contador
    # Modificamos o "text" do texto para apresentar o contador
    # strt(contador) transforma o numero em texto para ser apresentado
    texto["text"] = ("Contador: " + str(contador))
 
# Os elementos da interface botao e texto
botao = Button(janela, width = 4, text = "+1", command = clicou) # Em command, passamos a funcao criada para isso
botao.place(x = 110, y = 50) # O atributo place para posicionar
texto = Label(janela, text = "Vamos contar", bg = "#B0314C", fg = "#FFFFFF") # O texto, bg (cor de fundo) e fg (cor do texto)
texto.place(x = 90, y = 25) # O atributo place para posicionar
janela.title("Meu contador") # Titulo da janela
janela["bg"] = "#56A9DE" # Cor do fundo da janela "background"
janela.geometry("250x100+400+100") # Tamanho x,y e posicao da janela na tela
janela.mainloop()
print("A contagem acabou em: ", contador) # Apresenta no console a contagem final
