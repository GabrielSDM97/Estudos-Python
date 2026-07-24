# Dicionário de cores
cores = {
    'LIMPAR': '\033[m',
    'VERMELHO': '\033[91m',
    'VERDE': '\033[92m',
    'CIANO': '\033[96m'
}

''' Exercício 30 - Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR. '''

num = int(input(f'Insira um número:{cores['VERDE']} '))
print(cores['LIMPAR'])

if num%2 == 0:
    print(f'\nO número {num} é {cores['CIANO']}par{cores['LIMPAR']}.')
else:
    print(f'\nO número {num} é {cores['CIANO']}impar{cores['LIMPAR']}.')
print(12*f'{cores['VERMELHO']}-={cores['LIMPAR']}','FIM!',12*f'{cores['VERMELHO']}=-{cores['LIMPAR']}','\n')
