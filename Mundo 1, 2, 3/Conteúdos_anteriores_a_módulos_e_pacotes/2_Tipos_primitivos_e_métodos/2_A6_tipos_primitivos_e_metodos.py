# Tipos primitivos, Máscaras e Métodos.

'''

Existem 4 tipos primitivos em Python, são eles:

int = 1, 2, -4, 12930, ...
float = 2.5, -40.2941, ...
bool = True ou False.
str = 'José', 'Uma frase', '', '...'

Por padrão, será string qualquer variável sem um tipo primitivo definido, ou seja, "str".

'''

# É importantíssimo ultilizar os tipos primitivos, principalmente para fazer cálculos, veja baixo:
n1 = int(input('Digite o primeiro número: '))
# Utiliza-se "type()" para mostrar no terminal o tipo primitivo da variável após inserido um valor.
print({type(n1)},'\n') # \n = quebra de linha

n2 = int(input('Digite o segundo número: '))
print(type(n2),'\n')

n3 = input('Digite o terceiro número: ')
print(type(n3),'\n')

n4 = input('Digite o quarto número: ')
print(type(n4),'\n')

s1 = n1 + n2

s2 = n3 + n4

print('Com tipo primitivo "int()"')
print(f'A soma de {n1} e {n2} é {s1}.\n') 
# Em ".format()" ficaria: print('A soma de {} e {} é {}.'.format(n1, n2, s1))
# Sem nenhum metodo de formatação ficaria: print('A soma de', n1, 'e', n2, 'é', s1).

print('Com tipo primitivo "str()"')
print(f'A junção de {n3} com {n4} é {s2}.\n')

# Existem muitos outros métodos. Abaixo veremos um dos métodos de teste:
# variavel.isnumeric() - Metodo para verificar se o conteúdo da variável é numérico.
print(f's2 é numérico? {s2.isnumeric()}.\n') 
# Em .format(): print('s2 é numérico? {}.'.format(s2.isnumeric()))
# Nota-se que, apesar da variável "s2" ser uma string, o conteúdo dela é considerado numérico, podendo ser transformado em "int", por exemplo.'

# Metodo para verificar se o conteúdo da variável é alfabético: "variavel.isalpha()".
print(f's2 é alfabético? {s2.isalpha()}.\n')
# Nota-se que, apesar da variável "s2" ser uma string, o conteúdo dela não é considerado alfabético, já que são números.'

''' 
Existem muitos outros metodos de teste de tipo "is..." comos os citados acima, alguns exemplos:
isalnum (string + números)
isupper (letras maiúsculas)
etc...
'''
