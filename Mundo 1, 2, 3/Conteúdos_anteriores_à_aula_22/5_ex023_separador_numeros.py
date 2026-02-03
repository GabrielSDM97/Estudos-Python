''' Exercício 23 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. '''

num = int(input('Digite um número:\033[92m '))
print('\033[m')

unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print(f'Unidade: \033[96m{unidade}\033[m\nDezena: \033[96m{dezena}\033[m\nCentena: \033[96m{centena}\033[m\nMilhar: \033[96m{milhar}\033[m\n')
