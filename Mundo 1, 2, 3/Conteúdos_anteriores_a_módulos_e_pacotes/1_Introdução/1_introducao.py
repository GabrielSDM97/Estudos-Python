# Introdução

# Aspas simples (recomendado) ou duplas são utilizada para imprimirem strings (número, caracteres, letras, etc.)
print('1' + '2')  # O operador aritmético "+" aqui concatena as strings "grudando-as".
print('1' '2') # Aqui os valores ficam grudados também.
print('1', '2')  # Já a vírgula concatena adicionando um espaço entre as strings.


# Já para cálculos, não é utilizado aspas.
# O operador "+" aqui soma os valores.
print(1 + 2)
print()

# Variáveis
nome = 'José'  # nome RECEBE 'José'
sobrenome = 'Pereira'
idade = 20
peso = 80.5

print('Com vírgulas')
# Para imprimir variáveis de strings e valores numéricos seguidos um do outro, usa-se vírgula.
print(nome, sobrenome, idade, peso)
print()

print('Com "+"')
# O operador aritmético "+" serve para concatenar strings (ou variáveis com strings) ou para somar valores numéricos (ou variáveis com valores numéricos)
print(nome + sobrenome, idade + peso)


################################################################
# Existem duas formas de formatar strings no Python, são elas: #
################################################################

mundo = 'Mundo!'

''' 1. .format()
Metódo de formatação desenvolvido na versão 2.6 do Python. Atualmente é útil apenas por sua compatibilidade com versões mais antigas. '''
print('Olá {}'.format(mundo))
# É possível escolher a ordem dos argumentos dentro de format com números dentro das máscaras '{}', sendo 0 o primeiro argumento declarada no método.
print('{2} {1} {0}.'.format('A', 'B', 'C'))

''' 2. f-string
Metódo de formatação desenvolvido na versão 3.6 do Python. É o metodo mais moderno e recomendado por sua legibilidade, performance e por ser conciso. '''
print(f'Olá {mundo}')
