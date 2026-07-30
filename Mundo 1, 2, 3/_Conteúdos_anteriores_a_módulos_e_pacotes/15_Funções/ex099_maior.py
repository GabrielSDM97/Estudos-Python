from time import sleep
from random import randint

''' Exercício 99 - Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e dizer qual deles é o maior. '''


def maior(*num): 
    print('Analisando os valores passados',end='')
    for c in range(3):
        print('.',end='', flush = True)
        sleep(0.75)
    print()
    print(f'Foram analisados {len(num)} números.')
    print(f'O maior número é {max(num)}.\n')


# Programa principal
maior(5, 4, 7, 3, 1)
maior(8, 9, 2, 7)
maior(0, 6, 5)
maior(10, 9)
maior(1)

'''
def maior(*num):
    print('Analisando os valores passados',end='')
    for c in range(3):
        print('.',end='', flush = True)
        sleep(1)
    print()
    maior = 0
    for pos, número in enumerate(num):
        if pos == 0:
            maior = número
        elif número > maior:
            maior = número
    print(f'Forma analisados {len(num)} números.')
    print(f'O maior número é {maior}.')

        
# Programa principal
maior(5, 4, 7, 3, 1)
maior(8, 9, 2, 7)
maior(0, 6, 5)
maior(10, 9)
maior(1) '''
