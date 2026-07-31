''' Exercício 109 - Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, 
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108. '''

import moeda

valor = float(input('Valor: R$'))
porc_aum = 90
porc_red = 90

print(f'\nAcrescendo {porc_aum}% = {moeda.aumentar(valor, porc_aum)}')
print(f'Reduzindo {porc_red}% = {moeda.diminuir(valor, porc_red)}')
print(f'Dobro de {moeda.moeda(valor)} = {moeda.dobro(valor, True)}')
print(f'Metade de {moeda.moeda(valor)} = {moeda.metade(valor, True)}')

# help(moeda)
