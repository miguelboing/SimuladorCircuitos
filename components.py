
""" This module contains the input, output and all the logic gates classes used in the simulador. """

#------------------------------------------------------------------------ Class Declaration for Logic Gate Components ------------------------------------------------
# The Component class needs a wire method in order to link logic gates with other logic gates, inputs and outputs.

class Component:
    def __init__(self, *entry):
        self.entry = list(entry)
    
    def add_entry(self, *values):
        for value in values:
            self.entry.append(value)
        
class Or(Component):
    #def __init__(self,**kwargs):
        #super().__init__(**kwargs)
        #self.logic_value = exit()
        #print('OPA')

    @property
    def exit(self):
        return any(self.entry)
    
class And(Component):
    @property
    def exit(self):
        return all(self.entry)

class Not(Component):
    @property
    def exit(self):
        return not self.entry[0]

class Nand(Component):
    @property
    def exit(self):
        return not all(self.entry)

class Nor(Component):
    @property
    def exit(self):
        return not any(self.entry)

class Xor(Component):
    @property
    def exit(self):
        if all(self.entry) or not any(self.entry):
            return False
        return True


#------------------------------------------------------------------------ Class Declaration for Inputs and Outputs ---------------------------------------------------
# It would be interesting to create a method to update all the Outputs when an Inputs has his local_state changed.


class Input(): 
    def __init__(self, exit= False):
       self.exit = exit


class Output(Component):
    @property
    def exit(self):
        if any(self.entry):
            return True
        return False
    



# Bateria de testes
#porta = Nor(1,0,1)
#print(porta.exit)
#print(porta.entry)
#porta.add_entry(1,1,1,1)
#print(porta.exit)
#print(porta.entry)

