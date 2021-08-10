from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class Hello(App): #Nome da pasta onde estão os arquivos a serem exibidos (imagem)
    def build(self): #Essa função serve como a raiz da aplicação
        Window.size = (400, 300) #Tamanho da janela x,y
        self.window = GridLayout()
        self.window.cols = 1 
        self.window.size_hint = (0.9, 0.9) #Escala dos objetos da borda da janela x,y (0 à 1)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5} #Escala dos objetos no centro da janela x,y (0 à 1)
        #add widgets to window
        self.window.add_widget(Image(source="logo.png")) #image widget
        self.greeting = Label(text="Qual o seu Nome?", font_size = 34, color='#FF0000') #label widget
        self.window.add_widget(self.greeting)
        self.user = TextInput(multiline=False, padding_y = (10,10), size_hint = (1, 0.4)) # Posição e tamanho da caixa de texto
        self.window.add_widget(self.user)
        #button  widget
        self.button = Button(text="Gerar Frase", size_hint=(1,0.3), bold = True, background_color ='#000FCE', background_normal = "")
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)
        return self.window
    def callback(self, instance):
        self.greeting.text = "Olá " + self.user.text + "!" 

if __name__ == "__main__":
    Hello().run()
