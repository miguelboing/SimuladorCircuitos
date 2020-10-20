#import components

from kivy.app import App
import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.uix.behaviors import DragBehavior

kivy.require('1.11.1')

# Criando as classes para cada uma das telas
class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    pass

class Interface_G(Screen):
    def addComponent(self):
        self.ids.workflow.add_widget(Comp()) # Método para criar componentes
class Info(Screen):
    pass 

class Comp(DragBehavior, Widget): #Classe contendo atributos dos componentes
    pass


# Classe com o método para rodar o App
class Simulador(App):
    def build(self):
        return Gerenciador()

# Rodando o programa
if __name__ == '__main__':
    Simulador().run()

