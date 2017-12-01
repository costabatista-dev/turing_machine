from n_turing_machine import turing_machine
import LeitorArquivo as LA
import sys

def main():
    if len(sys.argv) < 3:
        print("Parametros insuficientes. Informe o nome de arquivo de entrada (.txt)")
        sys.exit(1)
    la = LA.LeitorArquivo(sys.argv[1])
    if la.get_number_of_tapes() != len(sys.argv)-2:
        print("Atenção!, numero de fitas nao condizem com a quantidade de argumentos passados")
    if (len(sys.argv)-2) > la.get_number_of_tapes():
        exit(0)

    
    m = turing_machine(la.get_initial(),la.get_final_states(), la.get_transitions(), la.get_whitespace(), la.get_number_of_tapes())

    inputs = [sys.argv[i] for i in range(2, len(sys.argv))]

    m.set_input(inputs)
    print(m.run())

if __name__ == "__main__":
    main()





