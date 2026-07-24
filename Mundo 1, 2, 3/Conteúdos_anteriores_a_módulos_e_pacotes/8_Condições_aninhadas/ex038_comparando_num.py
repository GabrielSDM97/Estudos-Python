# Variáveis de cores
limpar = '\033[m'
verde = '\033[92m'

''' Exercício 38 - Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais '''

num1 = int(input(f'Insira o primeiro valor:{verde} '))
num2 = int(input(f'{limpar}Insira o segundo valor:{verde} '))
print(limpar)

if num1 > num2:
    print('O primeiro valor é maior.')
elif num1 < num2:
    print('O segundo valor é maior.')
else:
    print('Não existe valor maior, os dois são iguais!')
