from tape import tape

class ntapes(object):
    def __init__(self, whitespace, amount, input_value=None):
        # Ternaria y = x > 0 ? x : 1
        self.amount = amount if amount > 0 else 1
        self.whitespace = whitespace
        self.tapes = []
        if input_value != None:
            self.set_tapes(input_value)
        else:
            self.set_tapes(whitespace)            

    def set_tapes(self, input_values):
        # Cria n fitas ou reseta todas com uma nova entrada
        self.tapes = [tape(self.whitespace) for i in range(self.amount)]
        if type(input_values) == type([]) and len(input_values) == self.amount:
            for i in range(len(input_values)):
                self.tapes[i].set_all_content(input_values[i])
        
    def get_contents(self):
        return [s.get_content() for s in self.tapes ]

    def set_content_and_move_head(self, symbols, movements):
        # Se o tamanho das listas symbols e movements condizem com a quantidade de fitas
        if len(symbols) == len(movements) and len(symbols) == self.amount:
            for i in range(self.amount):
                self.tapes[i].set_content(symbols[i])
                self.tapes[i].move_head(movements[i])

    def print(self):
        string = ""
        for tape in self.tapes:
            for i in tape.content:
                string += i
            print(string)
            string = ""

'''
nt = ntapes("B", 2, "abcde")
nt.print()
'''
