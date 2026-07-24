# Variáveis de cores
limpar = '\033[m'
negrito = '\033[1m'
vermelho = '\033[91m'
verde = '\033[92m'
amarelo ='\033[93m'
ciano = '\033[96m'

''' Exercício 52 -  Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. '''

num = int(input(f'Insira um número:{verde} '))
print(limpar)
contador_resto_0 = 0

if num > 1:
    for contador in range(1, num+1):
        if num % contador == 0:
            contador_resto_0 += 1
            print(f'{amarelo}{contador}{limpar}',end=' ')
        else:
            print(f'{ciano}{contador}{limpar}',end=' ')
    if contador_resto_0 > 2:
        print(f'\n\nO número {num} {vermelho}não é primo{limpar}, já que existem {contador_resto_0} divisões com resto 0 entre 1 e ele mesmo.\n')
    else:
        print(f'\n\nO número {num} {verde}é primo{limpar}, pois existem apenas 2 divisões com resto 0, sendo 1 e ele mesmo.\n')
else:
    print(f'O número {num} não é maior que 1, ou seja, não é primo.')
