''' Exercício 4 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele. '''

algo = input("Digite algo: ")

print(f'O tipo primitivo deste valor é \033[92m{type(algo)}\033[m')
print(f'Só tem espaços? \033[92m{algo.isspace()}\033[m')
print(f'É um número? \033[92m{algo.isnumeric()}\033[m')
print(f'É alfabético? \033[92m{algo.isalpha()}\033[m')
print(f'É alfanumérico? \033[92m{algo.isalnum()}\033[m')
print(f'Está em maiúsculas? \033[92m{algo.isupper()}\033[m')
print(f'Está em minúsculas? \033[92m{algo.islower()}\033[m')
print(f'Está capitalizado? \033[92m{algo.istitle()}\033[m')
