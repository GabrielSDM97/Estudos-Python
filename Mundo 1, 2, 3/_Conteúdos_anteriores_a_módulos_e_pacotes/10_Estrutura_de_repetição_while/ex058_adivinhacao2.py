import random
from time import sleep

# Variáveis de cores
limpar = '\033[m'
verde = '\033[92m'
ciano = '\033[96m'

''' Exercício 58 - Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer. '''

numero_aleatorio = random.randint(0, 10)
numero = int(input(f'Tente adivinhar o número que eu pensei de 0 a 10:{verde} '))
print(limpar)
tentativas = 1
print('Analisando o número inserido...\n')
sleep(1.5)

while numero != numero_aleatorio:
    tentativas += 1
    if numero < numero_aleatorio:
        numero = int(input(f'É maior... Tente novamente:{verde} '))
        print(limpar)
    else:
        numero = int(input(f'É menor... Tente novamente:{verde} '))
        print(limpar)
    print('Analisando o número inserido...\n')
    sleep(1.5)
print(f'Parabéns, você acertou após {ciano}{tentativas}{limpar} tentativas!')
