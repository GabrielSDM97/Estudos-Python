import random
from time import sleep

''' Exercício 28 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir 
qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu. '''

numero_aleatorio = random.randint(0, 5)
numero = int(input('Tente adivinhar o número que eu pensei de 0 a 5:\033[92m '))
print('\033[m')
print('Analisando o número inserido...\n')
sleep(1.5)

if numero == numero_aleatorio:
    print('Parabéns, você acertou!')
else:
    print(f'Infelizmente você errou, o número que eu escolhi era \033[96m{numero_aleatorio}\033[m!!')
