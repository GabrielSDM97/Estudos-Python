# Variáveis de cores
limpar = '\033[m'
verde = '\033[92m'
ciano = '\033[96m'

''' Exercício 72 - Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso. '''

numero = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco',
    'seis', 'sete', 'oito', 'nove', 'dez',
    'onze', 'doze', 'treze', 'quatorze', 'quinze',
    'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
)

while True:
    num_inserido = int(input(f'\n{limpar}Digite um número:{verde} '))
    if 0 <= num_inserido <= 20:
        print(f'{limpar}O valor inserido foi {ciano}{numero[num_inserido]}{limpar}!')
    else:
        print(f'{limpar}Valor não identificado na túpla!')
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input(f'\n{limpar}Deseja inserir um novo número? [S/N]{verde} '))
        if continuar not in 'SsNn':
            print(f'{limpar}Resposta inválido, tente novamente!')
    if continuar in 'Nn':
        break
print(f'\n{limpar}Até mais!')
