# Variáveis de cores
limpar = '\033[m'
negrito = '\033[1m'
verde = '\033[92m'
ciano = '\033[96m'

''' Exercício 44 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros '''

print(10*'=','LOJAS GUANABARA',10*'=')

valor = float(input(f'Valor da compra: {verde}R$'))
modo_pagamento = int(input(f'{limpar}Condições de pagamento:\n1 - À vista com dinheiro/cheque\n2 - À vista no cartão\n3 - Em até 2x no cartão\n4 - 3x ou mais no cartão\nEscolha:{verde} '))
print(limpar)

print(f'O valor inicial da sua compra é de R${valor:.2f}!\n')

if modo_pagamento == 1:
    print(f'{negrito}{ciano}À vista no dinheiro ou cheque{limpar} o valor final será de R${valor * 0.9:.2f}!')
elif modo_pagamento == 2:
    print(f'{negrito}{ciano}À vista no cartão{limpar} o valor final será de R${valor * 0.95:.2f}!')
elif modo_pagamento == 3:
    print(f'O valor final será de R${valor:.2f} parcelado em {negrito}{ciano}2x{limpar} de R${valor / 2:.2f}!')
elif modo_pagamento == 4:
    parcelas = int(input(f'Digite a quantidade de parcelas:{verde} '))
    print(f'{limpar}')
    if parcelas >= 3:
        print(f'O valor final será de R${valor * 1.20:.2f} parcelado em {negrito}{ciano}{parcelas}x{limpar} de R${(valor * 1.20) / parcelas:.2f}!')
    else:
        print('Quantidade de parcelas inválida, tente novamente!')
else:
    print('Condição de pagamento inválida, tente novamente!')
print(40*'==')
