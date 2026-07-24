''' Exercício 12 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto. '''

valor = float(input('Digite um valor de um produto:\033[92m R$'))

print('\033[m')
print(f'O valor R${valor} com desconto de 5% fica R${(valor * 0.95):.2f}.')
