from turing_machine import turing_machine
import sys
from tape import tape


if __name__ == "__main__":
    fp = open(sys.argv[1], "r")
    lines_cmd = fp.readlines()
    lines = []
    for line in lines_cmd:
        lines.append(line.replace('\n',''))

    # Recebe os inputs do terminal
    input_alphabet = lines[0].split()
    tape_alphabet = lines[1]
    whitespace = lines[2].replace('\n','')
    states = lines[3].split()
    initial_state = lines[4]
    final_states = lines[5].split()
    number_of_tapes = lines[6]
    number_of_lines = len(lines)  # Sem necessidade

    # Pode ser substituido por
    '''
    transitions = []

    for i in range(7, number_of_lines):
        transitions.append(lines[i].split())
    '''
    transitions = [ i.split() for i in lines[7:] ]
    # Mas fica a critério
    
    # Fim get inputs

    number_of_args = 2 + int(number_of_tapes)
    
    # tape_list = tape(whitespace, tape_alphabet, [])
    # Porque definir uma fita sem content? Por padrao, ja é vazia.
    tape_list = tape(whitespace, tape_alphabet)

    # Essa execução esta fazendo o que mesmo?
    
    for i in range(2, number_of_args):
        tape_list.content = list(sys.argv[i])
    
    ###
    # Como a turing machine precisa executar varias entradas
    # seu conteudo deve ser atualizado para cada entrada...
    # Este código esta colocando todos os argumentos que seriam
    # para cada entrada, numa unica fita

    # Neste caso, é necessario um set_content() em turing_machine
    

    # Vou modificar um pouco a inicialização da turing_machine    
    # tm = turing_machine(states, final_states, initial_state, transitions, whitespace, [tape_list])
    tm = turing_machine(states, final_states, initial_state, transitions, whitespace)
    tm.set_input(str(sys.argv[2]))
    #print(tm.input)

    print(tm.run())
    #tm.run()
    # Vou passar isto para a função run
    '''
    for state in tm.final_states:
        if tm.current_state == state:
            print(True)
            exit(0)
    print(False)
    '''

