from leiaNum import leiaInt, leiaFloat

''' Exercício 113 - Reescreva a função leiaInt() que fizemos no desafio 104, 
incluindo agora a possibilidade da digitação de um número de tipo inválido. 
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade. '''

# Programa principal
n1 = leiaInt('\nDigite um valor inteiro: ')
n2 = leiaFloat('\nDigite um valor real: ')
print(f'\n\033[mO valor inteiro inserido foi \033[92m{n1}\033[m, e o real \033[92m{n2}\033[m!')
