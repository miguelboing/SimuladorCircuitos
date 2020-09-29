from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

# Criando as classes para cada uma das telas
class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    pass

class Interface_G(Screen):
    pass

class Info(Screen):
    pass 

# Classe com o método para rodar o App
class Simulador(App):
    def build(self):
        return Gerenciador()

# Rodando o programa
if __name__ == '__main__':
    Simulador().run()

