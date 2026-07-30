# Variáveis de cores
limpar = '\033[m'
verde = '\033[92m'
amarelo = '\033[93m'
magenta = '\033[95m'

''' Exercício 37 - Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 
1 para binário, 2 para octal e 3 para hexadecimal. '''

num = int(input('Digite um número inteiro: '))
base = int(input(f'Escolha a base de conversão: \n{verde}1 - binário{limpar}\n{amarelo}2 - octal{limpar}\n{magenta}3 - hexadecimal{limpar}\nSua escolha: '))

# Coloquei o metodo de fatiamento de string [2:] em todas as condições para pular os marcadores iniciais "0b", "0o" e "0x" dessas conversões.
if base == 1:
    print(f'\nO número {num} em binário é {verde}{bin(num)[2:]}{limpar}.') 
elif base == 2:
    print(f'\nO número {num} em octal é {amarelo}{oct(num)[2:]}{limpar}.')
elif base == 3:
    print(f'\nO número {num} em hexadecimal é {magenta}{hex(num)[2:]}{limpar}.')
else:
    print('Opção inválida, tente novamente!')
print('\n',12*'-=','FIM!',12*'=-')
