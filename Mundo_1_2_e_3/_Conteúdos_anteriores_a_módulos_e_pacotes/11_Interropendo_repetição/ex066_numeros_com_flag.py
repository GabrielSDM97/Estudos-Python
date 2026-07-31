# Variáveis de cores
limpar = '\033[m'
verde = '\033[92m'

''' Exercício 66 - Crie um programa que leia números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag). '''

contador = soma = 0

while True:
    num = int(input(f'{limpar}Digite um valor [999 para parar]:{verde} '))
    if num != 999:
        contador += 1
        soma += num
    else:
        break
print(f'{limpar}Foram digitados {contador} valores. A soma de todos eles é {soma}.')
