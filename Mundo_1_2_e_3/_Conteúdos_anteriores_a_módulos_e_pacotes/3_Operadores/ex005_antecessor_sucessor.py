''' Exercício 5 - Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor. '''

num = int(input('Insira um número: '))

# Forma mais concisa e eficiente de fazer utilizando apenas uma variável.
print(f'Antecessor de {num} é \033[91m{num - 1}\033[m. Já seu sucessor é \033[92m{num + 1}\033[m.')
