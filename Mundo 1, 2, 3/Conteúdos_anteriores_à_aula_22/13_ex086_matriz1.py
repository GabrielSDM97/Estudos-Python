# Variáveis de cores
limpar = '\033[m'
verde = '\033[92m'
ciano = '\033[96m'

''' Exercício 86 - Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. 
No final, mostre a matriz na tela, com a formatação correta. '''

# Minha resolução

'''
pos = [0,0]
matriz = []

for i in range(0,9):
    valor = int(input(f'Digite um valor para {pos}: '))
    matriz.append(valor)
    if pos[0] == 0 or pos[0] == 1 or pos[0] == 2:
        pos[1] += 1
    if pos[1] == 3:
        pos[0] += 1
        pos[1] = 0
print()
for i in range(0,9):
    if i == 3 or i == 6:
        print(f'\n[{matriz[i]:^6}]',end=' ')
    else:
        print(f'[{matriz[i]:^6}]',end=' ')
'''

# Resolução do Guanabara (Mais concisa e eficiente)

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'{limpar}Digite um valor para [{linha}, {coluna}]:{verde} '))
print(limpar)
print(12*'-=-')
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{ciano}{matriz[linha][coluna]:^6}{limpar}]', end=' ')
    print()
