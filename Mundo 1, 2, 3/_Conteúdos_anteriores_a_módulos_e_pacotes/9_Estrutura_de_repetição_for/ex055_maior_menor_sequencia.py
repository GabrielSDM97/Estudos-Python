# Variáveis de cores
limpar = '\033[m'
negrito = '\033[1m'
verde = '\033[92m'

''' Exercício 55 -  Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos. '''

maior_peso = menor_peso = 0

for pessoa in range(1,6):
    peso = float(input(f'Peso da {pessoa}ª pessoa: KG{verde} '))
    print(limpar)
    if pessoa == 1: # O primeiro valor inserido é o maior e o menor ao mesmo tempo.
        maior_peso = peso
        menor_peso = peso
    else: # A partir do segundo valor inicia-se a filtragem entre maior e menor.
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print(f'A pessoa mais leve pesa "{negrito}{menor_peso}KG{limpar}", e a mais pesada pesa "{negrito}{maior_peso}KG{limpar}".')

if maior_peso == menor_peso:
    print('Todas os pesos são iguais.')
