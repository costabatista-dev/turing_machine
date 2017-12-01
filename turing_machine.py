from tape import tape

class turing_machine:

    """A class to represent a turing machine."""
    def __init__(self, state_list, final_state_list, first_state, transition_list, whitespace_symbol):
        self.states = state_list
        self.initial_state = first_state
        self.final_states = final_state_list
        self.transitions = transition_list
        self.whitespace = whitespace_symbol
        self.input = []
        # Para recursao funcionar estas variaveis devem ser globais
        self.current_state = first_state
        self.tape = tape(whitespace_symbol)

    def run(self):
        self.tape = tape(self.whitespace, self.input)
        while self.step():
            ''' just a empty while function that executes turing machine's steps'''

        for state in self.final_states:
            if self.current_state == state:
                return True
        return False

    def step(self):
        for transition in self.transitions:
            if int(self.current_state) == int(transition[0]) and self.tape.get_content() == transition[2]:
               
                self.tape.set_content(transition[3])
                self.current_state = transition[1]
                self.tape.move_head(transition[4])
               
                return 1
        return 0

    # -------------------------------------------------- 
    def set_input(self, input_value):
        self.input = [i for i in input_value]
