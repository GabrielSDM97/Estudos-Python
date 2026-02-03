''' Exercício 110 - Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), 
que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui. '''

import moeda

valor = float(input('Valor: R$'))

moeda.resumo(valor, 90, 80, True)

print()

# help(moeda.resumo)
