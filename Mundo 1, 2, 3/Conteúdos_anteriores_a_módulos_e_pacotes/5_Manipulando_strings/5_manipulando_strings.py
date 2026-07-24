''' Manipulando textos

Uma string é composta de posições, as quais são preenchidas por caracteres e espaços em branco, exemplo:

var = 'curso de python'

Acima temos uma string com 15 posições preenchidas sendo o primeiro 0 e o último 14.

Abaixo veremos as diferentes formas de manipular esses itens.

'''

# Fatiamento (range)

print(10*'-=-', 'Fatiamento', 10*'-=-', '\n')

string = '  curso de; python  '

print(f'String original: "{string}"\n')

print(f'Caractere na posição 2: "{string[2]}"\n')

print(f'Caractere na última posição: "{string[-1]}"\n')

print(f'Caracteres da posição 1 até a posição 3: "{string[1:4]}"\n')

print(f'De 1 até 9, pulando de 3 em 3 posições: "{string[1:10:3]}"\n')

print(f'Da posição 0 até 4: "{string[:5]}"\n')

print(f'Da posição 5 até a última posição da string: "{string[5:]}"\n')

print(f'Da posição item 5 até a última posição da string pulando de 2 em 2 posições: "{string[5::2]}"\n')

print(f'Mostra comprimento total da string em posições: "{len(string)}"\n')

print(f'Mostra a quantidade que um caractere aparece na string: "{string.count('o')}"\n')

print(f'Quantidade do caractere "o" de 0 até 14.: "{string.count('o', 0, 15)}"\n')

print(f'Em qual posição está a primeira letra "o" na string: "{string.find('o')}"\n')

print(f'Em qual posição está a última letra "o" na string: "{string.rfind('o')}"\n')

print(f'Se um termo está na string (Booleano).: "{'de' in string}"\n')

print(f'Se a string começa com o termo definido nos parâmetros (Booleano): "{string.startswith('  curso')}"\n')

print(f'Se a string termina com o termo definido nos parâmetros (Booleano): "{string.endswith('python  ')}"\n')

print(f'Troca um termo por outro na string apenas durante a execução da função, já que strings são imutáveis: "{string.replace('python', 'java')}"\n')

print(f'Transforma todas as minúsculas em maiúsculas: "{string.upper()}"\n')

print(f'Transforma todas as maiúsculas em minúsculas: "{string.lower()}"\n')

print(f'Transforma o primeiro caractere na string em maiúscula e o resto minúsculas: "{string.capitalize()}"\n')

print(f'Transforma o primeiro caractere de cada palavra na string em maiúscula e o resto em minúsculas: "{string.title()}"\n')

print(f'Remove espaços inúteis a esquerda e direita da string: "{string.strip()}"\n')

print(f'Remove espaços inúteis a direita da string: "{string.rstrip()}"\n')

print(f'Remove espaços inúteis a esquerda da string: "{string.lstrip()}"\n')


# Divisão

print(15*'--', 'Divisão', 15*'--', '\n')

print(f'Divide uma string em substrings. Por padrão o separador será cada instância de espaço em branco: "{string.split()}"\n')

print(f'É possível definir, nos parâmetros, um caractere como separador. Uma separação ocorrerá todas as vezes que o caractere apareçer na string: "{string.split(';')}"\n')


# Junção

print(15*'--', 'Junção', 15*'--', '\n')

# O método `separador.join(iterável)` é mais utilizado para transformar listas/tuplas/dicionários em strings, adicionando
# o separador, o qual também deve ser uma string, entre cada item de um objeto iterador.
# Quando utilizado em uma string, adiciona o separador entre cada posição dela, já que uma string é basicamente 
# um conjunto de posições sequenciais, cada uma tendo um caractere da string.

print(f'Adiciona caracteres entre cada posição na string: "{'_'.join(string)}"\n')


# Print longo

# --- Método 1: Strings Multi-linha (Triplas Aspas) ---
# Preserva a formatação original do código, incluindo quebras de linha e indentação.

print(15 * '--', 'Prints grandes', 15 * '--', '\n')

print("""Lorem Ipsum é simplesmente uma simulação de texto da indústria tipográfica e de impressos, e vem sendo utilizado desde o século XVI, 
quando um impressor desconhecido pegou uma bandeja de tipos e os embaralhou para fazer um livro de modelos de tipos. 
Lorem Ipsum sobreviveu não só a cinco séculos, como também ao salto para a editoração eletrônica, permanecendo essencialmente inalterado. 
Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de Lorem Ipsum, e mais recentemente quando passou a ser integrado 
a softwares de editoração eletrônica como Aldus PageMaker.\n""")

# --- Método 2: Concatenação Implícita de Strings ---
# O Python une strings separadas por espaços. O texto é impresso em linha contínua, ignorando as quebras de linha do código-fonte.

print("Lorem Ipsum é simplesmente uma simulação de texto da indústria tipográfica e de impressos, e vem sendo utilizado desde o século XVI, "
      "quando um impressor desconhecido pegou uma bandeja de tipos e os embaralhou para fazer um livro de modelos de tipos. "
      "Lorem Ipsum sobreviveu não só a cinco séculos, como também ao salto para a editoração eletrônica, permanecendo essencialmente inalterado. "
      "Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de Lorem Ipsum, e mais recentemente quando passou a ser integrado "
      "a softwares de editoração eletrônica como Aldus PageMaker.\n")


# É possível misturar diversas metodos de manipulação de texto, segue alguns exemplos abaixo:

print(15*'--', 'Manipulações com múltiplos métodos', 15*'--', '\n')

print(f'Quantidade da letra "O" maiúscula na string após transformar todas as letras em maiúsculas: "{string.upper().count('O')}"\n')

print(f'Comprimento da string após remover espaços inúteis a direita e esquerda dela: "{len(string.strip())}"\n')

print(f'Adiciona hífen entre cada substring: "{'-'.join(string.split())}"\n')

print(f'É possível escolher uma substring e depois posições dessa substring: "{string.split()[2][0::2]}"\n')


# É possível também utilizar metodos de manipulação de texto na criação de uma variável.

nome = str(input('Digite seu nome completo: ').strip().split()[0])

print(f'Seu primeiro nome é: {nome}')
