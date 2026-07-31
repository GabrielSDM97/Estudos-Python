''' Exercício 13 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento. '''

salario = float(input('Digite um salário:\033[92m R$'))

print('\033[m')
print(f'O salário de R${salario} com aumento de 15% fica R${(salario * 1.15):.2f}.')