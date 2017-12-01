#   0 Linha 1: alfabeto de entrada
#   1 Linha 2: alfabeto da fita
#   2 Linha 3: simbolo que representa um espaco em branco na fita
#   3 Linha 4: estado inicial
#   4 Linha 5, coloquem uma linha indicando o conjunto de estados de aceitacao
#   5 Linhas 6 em diante: transicoes, uma por linha, no formato
#   estado atual, simbolo atual,  novo estado, novo simbolo, direcao para mover a cabeca

class LeitorArquivo(object):
    def __init__(self, nomeArq):
	
        self.arq = open("{}".format(nomeArq), "r")
        buff = self.arq.read()
        linhas = buff.splitlines()


        self.AlfabetoEntrada = linhas[0]
        self.AlfabetoFita = linhas[1]
        self.EspacoBrancoFita = linhas[2]
        self.ConjuntoDeEstados = linhas[3].split(" ")
        self.EstadosIniciais = linhas[4]
        self.EstadoAceitacao = linhas[5].split(" ")

        transicoes = linhas[-1].split(" ")
        n = self.QF = (len(transicoes)-2) // 3
        
        transicoes = linhas[7:]
        self.Transicoes = []
        # 1, n... , 1 , n... , n...
        for t in transicoes:
            ax = t.split(" ")
            #print (ax)
            unit = [ ax[0], ax[1+n] ]
            sf = []
            psf = []
            dire = []
            if n == 1:
                self.Transicoes.append([ax[0], ax[1], [ax[2]], [ax[3]], [ax[4]]])
            else:
                for i in range(n):
                    sf.append(ax[ 1+i ])
                    psf.append(ax[ 2+n+i ])
                    dire.append(ax[ 2+(2*n)+i ])
                self.Transicoes.append( [unit[0], sf, unit[1], psf, dire] )
                    

    def get_input_alphabet(self):
        return self.AlfabetoEntrada

    def get_tape_alphabet(self):
        return self.AlfabetoFita

    def get_whitespace(self):
        return self.EspacoBrancoFita

    def get_initial(self):
        return self.EstadosIniciais

    def get_final_states(self):
        return self.EstadoAceitacao

    def get_transitions(self):
        return self.Transicoes

    def get_number_of_tapes(self):
        return self.QF
    def get_states_set(self):
        return self.ConjuntoDeEstados

### DEBUG
'''
la = LeitorArquivo("saida.txt")

print("Alfabeto da entrada")
print(la.get_input_alphabet())
print("Alfabeto da fita")
print(la.get_tape_alphabet())
print("Espaço branco da fita")
print(la.get_whitespace())
print("Conjunto de estados")
print(la.get_states_set())
print("Estado Inicial")
print(la.get_initial())
print("Estado(s) de aceitacao(s)")
print(la.get_final_states())
print("Quantidade de fitas")
print(la.get_number_of_tapes())
print("Transicoes")
ts = la.get_transitions()
for i in ts:
    print(i)
'''

