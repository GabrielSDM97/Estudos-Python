# Variáveis de cores
limpar = '\033[m'
verde = '\033[92m'
ciano = '\033[96m'

''' Exercício 77 - Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais. '''

tupla = ('Bolo', 'Vogal', 'Antena', 'Madeira', 'Anta')

for palavra in tupla:
    print(f'\nA palavra {verde}{palavra}{limpar} tem as seguintes vogais: ', end='')
    for letra in palavra:
        if letra in ('AaEeIiOoUu'):
            print(f'{ciano}{letra}{limpar}', end=' ')
