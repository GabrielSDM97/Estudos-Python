''' Exercício 23 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. '''

num = int(input('Digite um número:\033[92m '))
print('\033[m')

''' 
Todo resto de divisão por 10 retornará a casa da unidade de um dado número. 
Exemplo 1: 1136 % 10 = 6 (Unidade)

Seguindo essa lógica, 100 será Dezena+Unidade, 1000 Centena+Dezena+Unidade, e assim por diante.
Exemplo 2: 1136 % 100 = 36 (Dezena + Unidade)
Exemplo 3: 1136 % 1000 = 136 (Centena + Dezena + Unidade)

Para isolar uma casa decimal específica, divide-se o número da seguinte maneira:
Exemplo 1 (achar dezena): 1136 // 10 = 113, depois faz 113 % 10 = 3
Exemplo 2 (achar centena): 1136 // 100 = 11, depois faz 11 % 10 = 1
E assim por diante...
'''

unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print(f'Unidade: \033[96m{unidade}\033[m\nDezena: \033[96m{dezena}\033[m\nCentena: \033[96m{centena}\033[m\nMilhar: \033[96m{milhar}\033[m\n')
