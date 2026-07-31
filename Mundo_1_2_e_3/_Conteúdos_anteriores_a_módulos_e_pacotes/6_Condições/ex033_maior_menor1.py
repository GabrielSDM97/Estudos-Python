# Dicionário de cores
cores = {
    'LIMPAR': '\033[m',
    'VERMELHO': '\033[91m',
    'VERDE': '\033[92m',
    'MAGENTA': '\033[95m',
    'CIANO': '\033[96m'
}

''' Exercício 33 - Faça um programa que leia três números e mostre qual é o maior e qual é o menor. '''

num1 = float(input(f'Insira o primeiro número:{cores['VERDE']} '))
num2 = float(input(f'{cores['LIMPAR']}Insira o segundo número:{cores['VERDE']} '))
num3 = float(input(f'{cores['LIMPAR']}Insira o terceiro número:{cores['VERDE']} '))
print(cores['LIMPAR'])
num = None

# Com estrutura condicional
if num1 > num2 and num1 > num3:
    num = num1
elif num2 > num1 and num2 > num3:
    num = num2
else:
    num = num3
print(f'\nO maior número é {cores['CIANO']}{num:.2f}{cores['LIMPAR']},', end=' ')

if num1 < num2 and num1 < num3:
    num = num1
elif num2 < num1 and num2 < num3:
    num = num2
else:
    num = num3
print(f'e o menor é {cores['VERMELHO']}{num:.2f}{cores['LIMPAR']}.')

print(27*f'{cores['MAGENTA']}-=', f'{cores['LIMPAR']}')

# Forma mais compacta e eficiente
print(f'\nO maior número é {cores['CIANO']}{max(num1, num2, num3):.2f}{cores['LIMPAR']},', end=' ')
print(f'e o menor é {cores['VERMELHO']}{min(num1, num2, num3):.2f}{cores['LIMPAR']}.')
print(12*f'{cores['MAGENTA']}-=', f'{cores['LIMPAR']}FIM!', 12*f'{cores['MAGENTA']}=-', f'{cores['LIMPAR']}')
