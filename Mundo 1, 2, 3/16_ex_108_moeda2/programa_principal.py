''' Exercício 108 - Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado. '''

import moeda

valor = float(input('Valor: R$'))
porc_aum = 90
porc_red = 90

print(f'\nAcrescendo {porc_aum}% = {moeda.moeda(moeda.aumentar(valor, porc_aum))}')
print(f'Reduzindo {porc_red}% = {moeda.moeda(moeda.diminuir(valor, porc_red))}')
print(f'Dobro de {moeda.moeda(valor)} = {moeda.moeda(moeda.dobro(valor))}')
print(f'Metade de {moeda.moeda(valor)} = {moeda.moeda(moeda.metade(valor))}')
