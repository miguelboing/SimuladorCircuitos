""" This module contains the input, output and all the logic gates classes used in the simulador. """



#------------------------------------------------------------------------ Class Declaration for Inputs and Outputs ---------------------------------------------------
# It would be interesting to create a method to update all the Outputs when an Inputs has his local_state changed.

class Put:
    def __init__(self, logical_state=False):
        self.logical_state = logical_state


class Input(Put): 
    def change_logical_state(self):
        self.logical_state = not self.logical_state

class Output(Put):
    def show_logical_state(self):
        return self.logical_state



#------------------------------------------------------------------------ Class Declaration for Logic Gate Components ------------------------------------------------
# The Component class needs a wire method in order to link logic gates with other logic gates, inputs and outputs.

class Component:
    def __init__(self, *entry):
        self.entry = entry


class Or(Component):
    def exit(self):
        return any(self.entry)

class And(Component):
    def exit(self):
        return all(self.entry)

class Not(Component):
    def exit(self):
        return not self.entry[0]

class Nand(Component):
    def exit(self):
        return not all(self.entry)

class Nor(Component):
    def exit(self):
        return not any(self.entry)

class Xor(Component):
    def exit(self):
        if all(self.entry) or not any(self.entry):
            return False
        return True
