# Variáveis de cores
limpar = '\033[m'
negrito = '\033[1m'
verde = '\033[92m'
ciano = '\033[96m'

''' Exercício 93 - Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato. '''

gols = list()
jogador = dict()
jogador['Nome'] = str(input(f'Nome do jogador:{verde} '))
print(limpar)
partidas = int(input(f'{limpar}Quantas partidas {jogador['Nome']} jogou?{verde} '))
total_gols = 0
for c in range(0, partidas):
    gols.append(int(input(f'{limpar}Gols feitos na {c+1}ª partida:{verde} ')))
total_gols = sum(gols) # ou 'total_gols += gols[c]' dentro de 'for' acima.
jogador['Gols'] = gols[:]
jogador['Total de gols'] = total_gols
print(f'{limpar}\n'+20*'~~~')
print(jogador)
print(20*'~~~')
for chave, valor in jogador.items():
    if 'Gols' != chave != 'Partidas':
        print(f'{negrito}{chave}{limpar}: {ciano}{valor}{limpar}')
print(20*'~~~')
print(f'O jogador {jogador['Nome']} jogou {len(jogador['Gols'])} partidas!')
for c in range(0,len(jogador['Gols'])):
    print(f'{'=> ':>4}{negrito}{c+1}ª partida{limpar}: {ciano}{jogador['Gols'][c]}{limpar} gols!')
print(20*'~~~')
