from tape import tape

class turing_machine:

    """A class to represent a turing machine."""
    def __init__(self, state_list, final_state_list, first_state, transition_list, whitespace_symbol, tape_list=[]):
        self.tape_list = tape_list
        self.states = state_list
        self.initial_state = first_state
        self.final_states = final_state_list
        self.transitions = transition_list
        self.whitespace = whitespace_symbol
        self.current_state = first_state

    def move_head(self, tape_number, movement):
        if movement == 'L':

            self.tape_list[tape_number].move_left()
        elif movement == 'R':

            self.tape_list[tape_number].move_right()

    def run(self):
        self.tape_list[0].size = len(self.tape_list[0].content)
        while self.step():
            ''' just a empty while function that executes turing machine's steps'''


    def getElementAtPosition(self, position, tapeElement):

        if position >= 0 and position < tapeElement.size:
            return tapeElement.content[position]
        elif  position < 0:
            tapeElement.size += 1
             
            tapeElement.content.insert(0,self.whitespace)

        else:
            tapeElement.size += 1
            tapeElement.content.append(self.whitespace)
        return self.whitespace


    def step(self):
        for transition in self.transitions:
            head = int(self.tape_list[0].position)
 
            if int(self.current_state) == int(transition[0]) and self.getElementAtPosition(head, self.tape_list[0]) == transition[2]:
               
                self.tape_list[0].content[head] = transition[3]
                self.current_state = transition[1]
                self.move_head(0,transition[4])
               
                  
                return 1
        return 0
