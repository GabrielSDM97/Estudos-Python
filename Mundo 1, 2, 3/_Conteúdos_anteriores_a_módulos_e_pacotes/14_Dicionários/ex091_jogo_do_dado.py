from random import randint
from time import sleep

''' Exercício 91 - Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado. '''

jogo = dict()

for c in range(0, 4):
    jogo[f'jogador {c+1}'] = randint(1, 6)
    sleep(1)
    print(f'O jogador {c+1} tirou {jogo[f'jogador {c+1}']} no dado.')
rank = sorted(jogo.items(), key=lambda posição: posição[1], reverse=True)
print('\n'+15*'~'+'Rank'+14*'~')
for c in range(0, 4):
    print(f'{c+1}º lugar - {rank[c][0]} com {rank[c][1]} pontos.')
print(33*'~')
