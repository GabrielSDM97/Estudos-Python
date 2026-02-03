# Variáveis de cores
limpar = '\033[m'
verde = '\033[92m'
ciano = '\033[96m'

''' Exercício 71 - Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1. '''

contador_1 = contador_10 = contador_20 = contador_50 = 0

print(20*'~',f'\n{'Banco do povo':^20}')
print(20*'~')
while True:
    valor = int(input(f'\n{limpar}Insira o valor a ser sacado: {verde}R$'))
    while valor >= 50:
        valor -= 50
        contador_50 += 1
    while valor >= 20:
        valor -= 20
        contador_20 += 1
    while valor >= 10:
        valor -= 10
        contador_10 += 1
    while valor >= 1:
        valor -= 1
        contador_1 += 1
    print(limpar)
    print(20*'-',f'\n{'Saque':^20}')
    print(20*'-')
    print(f'{limpar}O valor foi sacado em:')
    if contador_50 >= 1:
        print(f'{ciano}{contador_50}{limpar} cédulas de {verde}R$50{limpar}!')
    if contador_20 >= 1:
        print(f'{ciano}{contador_20}{limpar} cédulas de {verde}R$20{limpar}!')
    if contador_10 >= 1:
        print(f'{ciano}{contador_10}{limpar} cédulas de {verde}R$10{limpar}!')
    if contador_1 >= 1:
        print(f'{ciano}{contador_1}{limpar} cédulas de {verde}R$1{limpar}!')
    contador_1 = contador_10 = contador_20 = contador_50 = 0
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input(f'\n{limpar}Deseja sacar um novo valor? [S/N]{verde} '))
        if continuar not in 'SsNn':
            print(f'{limpar}Resposta inválida, tente novamente!')
    if continuar in 'Nn':
        break
print(f'\n{limpar}Tenha um bom dia!')
