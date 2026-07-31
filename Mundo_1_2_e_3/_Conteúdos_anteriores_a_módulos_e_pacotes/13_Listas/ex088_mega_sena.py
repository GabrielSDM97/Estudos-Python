from random import randint
from time import sleep

# Variáveis de cores
limpar = '\033[m'
verde = '\033[92m'
amarelo = '\033[93m'
ciano = '\033[96m'

''' Exercício 88 - Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta. '''

# Minha Resolução

palpites = []
temp = []
jogos_qtd = int(input(f'Quantos jogos você quer?{verde} '))
print(limpar)
print(10*'~',f'Sorteando {amarelo}{jogos_qtd}{limpar} jogos!',10*'~')
for jogo in range(0, jogos_qtd):
    for num in range(0,6):
        num_aleatorio = randint(1,60)
        temp.append(num_aleatorio)
    palpites.append(temp[:])
    print(f'Jogo {jogo+1}: {ciano}{palpites[jogo]}{limpar}')
    sleep(1.5)
    temp.clear()
print(14*'~','BOA SORTE!',14*'~')
