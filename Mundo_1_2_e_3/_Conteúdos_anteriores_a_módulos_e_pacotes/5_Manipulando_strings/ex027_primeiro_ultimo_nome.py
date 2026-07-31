''' Exercício 27 - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. '''

nome = str(input('Insira seu nome completo:\033[92m ').strip())
print('\033[m')

print(f'\nSeu primeiro nome é \033[96m{nome.split()[0]}\033[m.\nSeu último nome é \033[96m{nome.split()[-1]}\033[m.')