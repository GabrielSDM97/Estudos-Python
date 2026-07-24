# Variáveis de cores
limpar = '\033[m'
verde = '\033[92m'

''' Exercício 65 - Evolução do DESAFIO 033. Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores. '''

contador = somatoria = media = maior = menor =  0
resposta = 'S'
while resposta not in 'nN':
    num = int(input(f'{limpar}Digite um número:{verde} '))
    contador += 1
    somatoria += num
    media = somatoria/contador
    if contador == 1: # O primeiro valor inserido é o maior e o menor ao mesmo tempo.
        maior = num
        menor = num
    else: # A partir do segundo valor inicia-se a filtragem entre maior e menor.
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input(f'{limpar}Quer continuar? [S/N]:{verde} ').strip()[0])
if maior == menor:
    print(f'{limpar}Você digitou {contador} números. A média de todos os valores é {media:.2f}. Todos os números são iguais')
else:
    print(f'{limpar}Você digitou {contador} números. A média de todos os valores é {media:.2f}. O maior é {maior}. O menor é {menor}')
