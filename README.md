## Máquina de Turing Não Determinística
 <p style="text-align: justify;">
 Este trabalho tem finalidade avaliativa na disciplina de <b>LINGUAGENS FORMAIS, AUTOMATOS E COMPUTABILIDADE (IC4A)</b> ministrada na <b>Universidade Tecnológica Federal do Paraná Campus Campo Mourão (UTFPR-CM)</b> e representa o trabalho prático (<b>APS</b>). Ele consiste em uma implementação de um programa que tem por finalidade representar uma máquina de turing <b>não determinística</b> de acordo com definições de entrada.</p>
<p style="text-align: justify;">
Por decisão de projeto, foi escolhido a linguagem de programação <b>Python</b>, em virtude de sua simplicidade para a realização das implementações. A versão <b>Python</b> utilizada foi a <b>3.6</b> provida pelo gerenciador de dependências <a href="https://anaconda.org/" target="_blank"><b>Anaconda</b></a>. 
</p>
### Como executar o programa
<p style="text-align: justify;">
 O programa da máquina de turing não possui interface gráfica, portanto sua execução se dá pela linha de comando. Dessa forma, temos a seguinte instrução para executá-lo:
 </p>
  
```bash
python3 main.py arquivo.txt  conteudo_fita_1 [conteudo_fita_2] ... [conteudo_fita_n] 
```

<p style="text-align: justify">
<ul>
 <li><b>arquivo.txt</b>: Arquivo de texto que define uma máquina de turing (saída do programa do professor)</li>
 <li><b>[conteudo_da_fita]</b>: Sequência de caracteres de entrada</li>
</ul>
</p>


### Os módulos

<p style="text-align: justify">
Dentre os módulos de código que compõem o software desenvolvido estão:
<ol>
 <li><b>main.py</b></li>
 <li><b>tape.py</b></li>
 <li><b>instance.py</b></li>
 <li><b>turing_machine.py</b></li>
</ol>

Estes serão aprofundadamente explicados a seguir.
</p>


### Tape.py
<p style="text-align: justify">
Esse módulo representa a entidade <b>fita</b>.  Tal módulo faz parte da máquina de turing. Seu construtor é definido da seguinte forma.
</p>


```python
  '''
        @param whitespace: espaço em branco
        @param tape_alphabet: alfabeto da fita
        @param content: conteúdo presente na fita
  '''
    def __init__(self, whitespace, tape_alphabet, content=[]):
        self.position = 0 # posicao atual da fita
        self.whitespace_symbol = whitespace
        self.alphabet = tape_alphabet
        self.content = content
        self.size = len(content) # tamanho da fita
```

<p style="text-align: justify">
A fita possui um método cuja funcionalidade é movimentar a posição (<b>cabeça</b>) da fita.
</p>
  
```python

 '''
    @param movement: movimento da fita → pode ser para esquerda (L) ou para direita (R)
 '''
    def move_head(self, movement):
        if movement == 'L': 
            self.move_left()
        elif movement == 'R':
            self.move_right()


```


<p style="text-align: justify">
Como pode ser observado, o método que movimenta a posição de uma fita tem duas possibilidades. A cabeça da fita é movida para a esquerda ou para a direita, dependendo da orientação da movimentação. Dessa forma, os métodos de movimentação que são executados
podem ser: <br/>

<ul>
 <li>Mover para esquerda: </li>
</ul>

 ```python
   def move_left(self):
        if self.position > 0: # se existir espaco pra esquerda, vai para a esquerda
            self.position -= 1
        else: # se nao, coloca um branco no comeco da fita
            self.content.insert(0,self.whitespace_symbol)
 ```
 
<ul>
 <li>Mover para a direita: </li>
</ul> 

 ```python
    def move_right(self): 
        if self.position < len(self.content)-1: # se tiver posicao para a direita, vai para a direita
            self.position += 1
        else: # se nao, coloca um espaco em branco na fita e vai para a direita
            whitespace = self.whitespace_symbol
            self.content.append(whitespace)
            self.position += 1
 ```
 

</p>

<p style="text-align: justify">
Além disso, na fita há métodos para obter o elemento da posição atual, bem como, para alterar o elemento da posição corrente.
Estes são:
</p>

<ul>

<li>Método para retornar o conteúdo da posição atual da fita: </li>
</ul>  
 
 ```python
    def get_content(self):
        return self.content[self.position]
  ```

<ul>  
<li>Método para modificar o conteúdo da posição atual da fita:</li>
</ul>
 
 ```python
     def set_content(self, symbol):
        self.content[self.position] = symbol 
 ```   
    

    




### Autores
**Paulo Batista - github.com/costabat** 
**Venancius Michelan**
