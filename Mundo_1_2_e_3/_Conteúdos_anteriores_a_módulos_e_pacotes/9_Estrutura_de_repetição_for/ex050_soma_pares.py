# Variáveis de cores
limpar = '\033[m'
verde = '\033[92m'
ciano = '\033[96m'


''' Exercício 50 -  Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
Se o valor digitado for ímpar, desconsidere-o. '''

soma_par = contador_paro = 0

for numero in range(1,7):
    num = int(input(f'Digite o {numero}º número:{verde} '))
    print(limpar)
    if num % 2 == 0:
        contador_par += 1
        soma_par += num
print(f'A soma dos {ciano}{contador_par}{limpar} números pares inseridos é {ciano}{soma_par}{limpar}.')
