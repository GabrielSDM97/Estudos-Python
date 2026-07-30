# Variáveis de cores
limpar = '\033[m'
verde = '\033[92m'

''' Exercício 64 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag, ou seja, o valor 999). '''

num = 0
soma_num = 0
contador = 0

num = int(input(f'Digite um valor [999 para parar]:{verde} ')) # Para inserir o valor inicial da variável "num", do contrário daria erro.
while num != 999:
    soma_num += num
    contador += 1
    num = int(input(f'{limpar}Digite um valor [999 para parar]:{verde} ')) # Por estar no fim do loop, se eu digitar '999', este valor não será somado na variável 'soma_num'.
print(f'{limpar}Foram digitados {contador} números, e a soma entre eles foi de {soma_num}.')
