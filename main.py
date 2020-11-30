from kivy.app import App
import kivy
from kivy.lang.builder import Builder
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
from kivy.properties import ListProperty
from kivy.properties import BooleanProperty

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
        self.pos1 = ListProperty(pos1)
        self.pos2 = ListProperty(pos2)
        print(pos1, pos2)
        print(self.pos1, self.pos2)

# -------------------------------------------------------------Classes de cada porta ----------------------------------------------------------------------

class Comp(DragBehavior, Widget): #Classe contendo atributos dos componentes
    def __init__(self, comp_name='',*entry, **kwargs):
        super().__init__()
        self.ids.comp_name_l.text = comp_name
        self.entry = ListProperty(*entry)

        print(*entry)
    
    def add_entry(self, *values):
        for value in values:
            self.entry.append(value)



class And(Comp):
    @property
    def exit(self):
        return all(self.entry)

class Or(Comp):
    @property
    def exit(self):
        return any(self.entry)

class Not(Comp):
    @property
    def exit(self):
        return not self.entry[0]

class Nand(Comp):
    @property
    def exit(self):
        return not all(self.entry)

class Nor(Comp):
    @property
    def exit(self):
        return not any(self.entry)

class Xor(Comp):
    @property
    def exit(self):
        if all(self.entry) or not any(self.entry):
            return False
        return True

class Input(Comp):
    def __init__(self):
        super().__init__()
        print('oi')
    def change_logical_state(self):
        self.exit = not self.exit
        


class Output(Comp):
    @property
    def exit(self):
        self.ids.o_logical_state_l.text = any(self.entry)
        print('estou funcionando')
        return any(self.entry)
  
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

# Classe com o método para rodar o App
class Simulador(App):
    pos2 = ListProperty([])
    def build(self):
        return Gerenciador()

# Rodando o programa
if __name__ == '__main__':
    Simulador().run()

