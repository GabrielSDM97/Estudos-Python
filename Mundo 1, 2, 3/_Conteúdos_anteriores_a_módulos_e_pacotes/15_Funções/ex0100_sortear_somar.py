from time import sleep
from random import randint

''' Exercício 100 - Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior. '''


def sorteia(sortear):
    print(f'Sorteando 5 valores: ',end='')
    for c in range(5):
        sortear.append(randint(0, 10))
        print(f'{sortear[c]},' if c < 4 else f'{sortear[c]}.', end=' ', flush = True)
        sleep(0.75)
    print()


def somaPar(lista):
    soma_par = 0
    for i in lista:
        if i % 2 == 0:
            soma_par += i
    print(f'Somando os valores pares da lista {lista}: {soma_par}')


# Programa principal
números = list()
sorteia(números)
somaPar(números)
