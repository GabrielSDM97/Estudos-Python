# Variáveis de cores
limpar = '\033[m'
verde = '\033[92m'

''' Exercício 63 - Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 

Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8  '''

termos = int(input(f'Quantos termos da sequência Fibonacci você quer mostrar?{verde} '))
print(limpar)
penúltimo = 0
último = 1

print(f'{penúltimo} → {último} → ',end='') # Posição 1 e 2 ( 0 - 1 da sequência Fibonacci)
posição = 3
while posição <= termos:
    atual = último + penúltimo
    print(f'{atual} →',end=' ')
    penúltimo = último
    último = atual
    posição += 1
print('FIM!\n')
