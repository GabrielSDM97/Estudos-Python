# Variáveis de cores
limpar = '\033[m'
vermelho = '\033[91m'
verde = '\033[92m'
ciano = '\033[96m'

''' Exercício 81 - Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista. '''


lista_valores = list()
while True:
    lista_valores.append (int(input(f'\n{limpar}Digite um valor:{verde} ')))
    continuar = ' '
    while True:
        continuar = str(input(f'{limpar}Deseja inserir mais um valor? [S/N]{verde} ').strip()[0])
        if continuar not in 'SsNn':
            print(f'\n{limpar}Resposta inválida, tente novamente!')
        else:
            break
    if continuar in 'Nn':
        break
lista_valores.sort(reverse = True)
print(f'\n{limpar}A) Quantos números foram digitados: {ciano}{len(lista_valores)}{limpar}')
print(f'B) A lista de valores, ordenada de forma decrescente: {ciano}{lista_valores}{limpar}')
print(f'C) Se o valor 5 está ou não na lista:', f'O valor 5 {verde}está na lista{limpar}!' if 5 in lista_valores else f'O valor 5 {vermelho}não está na lista{limpar}!')
