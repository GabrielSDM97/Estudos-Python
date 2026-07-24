# Dicionário de cores
cores = {
    'LIMPAR': '\033[m',
    'VERDE': '\033[92m',
    'CIANO': '\033[96m'
}

''' Exercício 34 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%. '''

salario = float(input(f'Digite um salário:{cores['VERDE']} '))
print(cores['LIMPAR'])
salario_final = None

if salario > 1250:
    salario_final = salario * 1.10
else:
    salario_final = salario * 1.15
print(f'Seu salário de R${salario:.2f}, com aumento, ficou {cores['CIANO']}R${salario_final:.2f}{cores['CIANO']}.')
