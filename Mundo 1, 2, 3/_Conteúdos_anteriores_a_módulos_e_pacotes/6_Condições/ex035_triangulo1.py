# Dicionário de cores
cores = {
    'LIMPAR': '\033[m',
    'VERMELHO': '\033[91m',
    'VERDE': '\033[92m',
    'CIANO': '\033[96m'
}

''' Exercício 35 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo. '''

lado_a = float(input(f'Primeiro segmento:{cores['VERDE']} '))
lado_b = float(input(f'{cores['LIMPAR']}Segundo segmento:{cores['VERDE']} '))
lado_c = float(input(f'{cores['LIMPAR']}Terceiro segmento:{cores['VERDE']} '))
print(cores['LIMPAR'])

if (lado_a + lado_b) > lado_c and (lado_a + lado_c) > lado_b and (lado_b + lado_c) > lado_a:
    print(f'Os seguimentos acima {cores['CIANO']}PODEM{cores['LIMPAR']} formar um triângulo.')
else:
    print(f'Os seguimentos acima {cores['VERMELHO']}NÃO PODEM{cores['LIMPAR']} formar um triângulo.')
