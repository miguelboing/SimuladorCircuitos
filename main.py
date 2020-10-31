import components

from kivy.app import App
import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.uix.behaviors import DragBehavior
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from kivy.uix.button import ButtonBehavior


kivy.require('1.11.1')


#cor de fundo das janelas
#Tema de cores - Brisk(#333D51 / #D3AC2B / #CBD0D8 / #F4F3EA) e Pebble(#433E49)
Cinza = "#333D51"  
Amarelo ="#D3AC2B"  
Creme = "CBD0D8"  
Branco = "F4F3EA"
#Site que tem uns temas legais -> https://www.shutterstock.com/blog/10-gorgeous-color-schemes-for-websites?kw=&gclsrc=aw.ds&gclid=CjwKCAjw0On8BRAgEiwAincsHCxfN4pB0eg2Do_bYEq_E9mtM6nkPacXiLYP9_mTEOm2mlOhHli3BBoCpLkQAvD_BwE
#se mudar a variavel muda a cor
Window.clearcolor = get_color_from_hex(Amarelo)

# Criando as classes para cada uma das telas
class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    pass

class Interface_G(Screen):

    def addComponent(self, comp_name= ''):  # Método para criar componentes
        if comp_name == 'AND':
            self.ids.workflow.add_widget(And(comp_name))
        elif comp_name == 'OR':    
            self.ids.workflow.add_widget(Or(comp_name))
        elif comp_name == 'NOT':    
            self.ids.workflow.add_widget(Not(comp_name))
        elif comp_name == 'NAND':    
            self.ids.workflow.add_widget(Nand(comp_name))
        elif comp_name == 'NOR':    
            self.ids.workflow.add_widget(Nor(comp_name))
        elif comp_name == 'XOR':    
            self.ids.workflow.add_widget(Xor(comp_name))
        elif comp_name == 'INPUT':    
            self.ids.workflow.add_widget(Input(comp_name))
        elif comp_name == 'OUTPUT':    
            self.ids.workflow.add_widget(Output(comp_name))

class Info(Screen):
    pass 


# -------------------------------------------------------------Classes de cada porta ----------------------------------------------------------------------

class Comp(DragBehavior, Widget): #Classe contendo atributos dos componentes
    def __init__(self, comp_name='', **kwargs):
        super().__init__()
        self.ids.comp_name_l.text = comp_name

class And(Comp, components.And):
    pass

class Or(Comp, components.Or):
    pass

class Not(Comp, components.Not):
    pass

class Nand(Comp, components.Nand):
    pass

class Nor(Comp, components.Nor):
    pass

class Xor(Comp, components.Xor):
    pass

class Input(Comp, components.Input):
    def change_logical_state(self):
        self.logical_state = not self.logical_state
        self.ids.i_logical_state_l.text = str(self.logical_state)


class Output(Comp, components.Output):
    pass


# --------------------------------------------------------------------------------------------------------------------------------------------------------------

# Classe com o método para rodar o App
class Simulador(App):
    def build(self):
        return Gerenciador()

# Rodando o programa
if __name__ == '__main__':
    Simulador().run()

