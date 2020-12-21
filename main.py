import components

from kivy.app import App
import kivy
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.uix.behaviors import DragBehavior
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from kivy.uix.button import ButtonBehavior
from kivy.properties import BooleanProperty
from kivy.properties import ListProperty
from kivy.graphics.vertex_instructions import Line
from kivy.graphics.context_instructions import Color
from kivy.uix.image import Image

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

    def addWire(self, pos1, pos2): # Método para criar fios
        self.ids.workflow.add_widget(Wire(pos1, pos2))    

class Info(Screen):
    pass 

# -------------------------------------------------------------Algorítimo criador de fios -----------------------------------------------------------------

class Wire(Widget):
    def __init__(self, pos1, pos2, **kwargs):
        super().__init__(**kwargs)
        self.pos1 = pos1
        self.pos2 = pos2
        with self.canvas:
            Color(0, 1, 0, 1)
            Line(points=[self.pos1[0] + 7,self.pos1[1]+ 7, self.pos2[0], self.pos2[1]+50], width=1)
        

# -------------------------------------------------------------Classes de cada porta ----------------------------------------------------------------------

class Comp(DragBehavior, Widget): #Classe contendo atributos dos componentes
    def __init__(self, comp_name='', **kwargs):
        super().__init__(**kwargs)
        self.comp_name = comp_name
        self.ids.comp_name_l.text = self.comp_name

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
        self.exit = not self.exit
        #self.ids.i_logical_state_l.text = str(self.exit)
        if str(self.exit) == "True":
            self.ids.i_logical_state_l.source = "images/gates/on.png"
        else:
            self.ids.i_logical_state_l.source = "images/gates/off.png"


class Output(Comp, components.Output):
    def update_label(self):
        #self.ids.o_logical_state_l.text = str(self.exit)
        if str(self.exit) == "True":
            self.ids.o_logical_state_l.source = "images/gates/lamp.on.png"
        else:
            self.ids.o_logical_state_l.source = "images/gates/lamp.off.png"
  
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

# Classe com o método para rodar o App
class Simulador(App):
    c = BooleanProperty(False)
    pos1 = ListProperty([])
    pos2 = ListProperty([])
    carg = BooleanProperty(False)
    text_1 = """    The main purpose of this project is to help beginners in the study of digital\n
    electronics, simulating combinatory circuits bringing theory to practice in a\n
    simple way.\n\n

    The software is designed specifically to help testing combinatorial circuits,\n
    and for now we don't have plans of adding sequencial circuits in future ver-\n
    sions.\n\n

    This project is still under development therefore there’s a lot to be implemen-\n
    ted, and bugs can eventually appear."""

    text_2 = """    This specific version is static, that means that the circuit cannot receive or up-\n
    date a component entry after the wire connections are created. This version\n
    is just a start and eventually will be obsolete with the launch of a dinamic ver-\n
    sion."""

    text_3 = """    That is very simple here’s the steps on how to create a circuit:\n\n

        1. Add all the inputs and set their values.\n\n

        2. Add the logic ports doing the wire connections left to right.\n\n

        3. Add the output ports, connect then to the ends of the circuit.\n\n

        Done, now you can check the outputs of the circuit!\n\n

    For more information go to: https://github.com/miguelboing/SimuladorCircuitos\n
    """

    def build(self):
        self.icon = 'images/logo2.png'
        self.title = 'simuGATE'
        return Gerenciador()

# Rodando o programa
if __name__ == '__main__':
    Simulador().run()
