from time import sleep

# Variáveis de cores
limpar = '\033[m'
negrito = '\033[1m'
vermelho = '\033[91m'
verde = '\033[92m'
amarelo = '\033[93m'
magenta = '\033[95m'
ciano = '\033[96m'

''' Exercício 59 - Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso. '''

num1 = float(input(f'1º Número:{verde} '))
num2 = float(input(f'{limpar}2º Número:{verde} '))
print(limpar)
opção = 0

while opção != 5:
    opção = int(input(f"""Escolha entre as 5 opções abaixo: 
{verde}[ 1 ]{limpar} {negrito}somar{limpar}
{amarelo}[ 2 ]{limpar} {negrito}multiplicar{limpar}
{ciano}[ 3 ]{limpar} {negrito}maior{limpar}
{magenta}[ 4 ]{limpar} {negrito}novos números{limpar}
{vermelho}[ 5 ]{limpar} {negrito}sair do programa{limpar}
Sua escolha?{verde} """))
    print(limpar)
    if opção == 1:
        print(20*f'-=-')
        soma = num1 + num2
        print(f'{f'Soma: {num1} + {num2} = {soma:.2f}':^60}')
        print(20*f'-=-','\n')
        sleep(2)
    elif opção == 2:
        print(20*f'-=-')
        produto = num1 * num2
        print(f'{f'Multiplicação: {num1} x {num2} = {produto:.2f}':^60}')
        print(20*f'-=-','\n')
        sleep(2)
    elif opção == 3:
        if num1 > num2:
            print(20*f'-=-')
            print(f'{f'{num1} é maior que {num2}':^60}')
            print(20*f'-=-','\n')
            sleep(2)
        elif num2 > num1:
            print(20*f'-=-')
            print(f'{f'{num2} é maior que {num1}':^60}')
            print(20*f'-=-','\n')
            sleep(2)
        else:
            print(20*f'-=-')
            print(f'{'Ambos são iguais.':^60}')
            print(20*f'-=-','\n')
            sleep(2)
    elif opção == 4:
        print('Você escolheu inserir novos números.')
        num1 = float(input(f'1º Número:{verde} '))
        num2 = float(input(f'{limpar}2º Número:{verde} '))
        print(limpar)
print('Você finalizou o programa. Até logo!')
