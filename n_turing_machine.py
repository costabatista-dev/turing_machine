from ntapes import ntapes

class turing_machine:
    """A class to represent a turing machine."""
    def __init__(self, first_state, final_state_list, transition_list, whitespace_symbol, quantity):
        self.quantity = quantity
        self.initial_state = first_state
        self.final_states = final_state_list
        self.transitions = transition_list
        self.whitespace = whitespace_symbol
        self.input = ""
        # Para recursao funcionar estas variaveis devem ser globais
        self.current_state = None
        self.tape = None

    def run(self):
        if self.input == "":
            return False
        self.current_state = self.initial_state
        self.tape = ntapes(self.whitespace, self.quantity, self.input)
        while self.step():
            ''' just a empty while function that executes turing machine's steps'''

        self.tape.print()
        
        for state in self.final_states:
            if self.current_state == state:
                return True
        return False

    def step(self):
        for transition in self.transitions:
            if int(self.current_state) == int(transition[0]) and self.tape.get_contents() == transition[2]:
                
                self.current_state = transition[1]
                self.tape.set_content_and_move_head(transition[3], transition[4])
                
                return 1
        return 0

    def set_input(self, input_value):
        self.input = [i for i in input_value]

'''
estados = [['0', '1', ['a'], ['b'], ['R']]]
tm = turing_machine(['0','1','2'], ['1'], '0', estados, 'B', 1)

tm.set_input("aaaa")
print(tm.run())
'''
