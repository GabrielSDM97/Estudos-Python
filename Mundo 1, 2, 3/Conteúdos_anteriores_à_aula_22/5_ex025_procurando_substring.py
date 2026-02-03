''' Exercício 25 - Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome. '''

nome = str(input('Digite seu nome completo:\033[92m ').upper().strip())
print('\033[m')

print(f'Seu nome tem "SILVA"? \033[96m{"SILVA" in nome.split()}\033[m')
