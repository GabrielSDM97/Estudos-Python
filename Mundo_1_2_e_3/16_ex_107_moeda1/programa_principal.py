''' Exercício 107 - Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
Faça também um programa que importe esse módulo e use algumas dessas funções. '''

import moeda

valor = float(input('Valor: R$'))
porc_aum = 90
porc_red = 90

print(f'\nAcrescendo {porc_aum}% = {moeda.aumentar(valor, porc_aum)}')
print(f'Reduzindo {porc_red}% = {moeda.diminuir(valor, porc_red)}')
print(f'Dobro de R${valor} = {moeda.dobro(valor)}')
print(f'Metade de R${valor} = {moeda.metade(valor)}')
