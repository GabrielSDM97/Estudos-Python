from datetime import date

# Variáveis de cores
limpar = '\033[m'
negrito = '\033[1m'
verde = '\033[92m'
amarelo = '\033[93m'
ciano = '\033[96m'

''' Exercício 54 - Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. '''

contador_maior = contador_menor = 0

for pessoa in range(1,8,1):
    ano_nascimento = int(input(f'Digite o ano de nascimento da {pessoa}ª pessoa:{verde} '))
    print(limpar)
    idade = date.today().year - ano_nascimento
    if idade >= 21:
        contador_maior += 1
    else:
        contador_menor += 1
print(f'{negrito}{contador_maior}{limpar} pessoa/pessoas são de maior, enquanto {negrito}{contador_menor}{limpar} pessoa/pessoas são de menor.')
