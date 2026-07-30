# Variáveis de cores
limpar = '\033[m'
negrito = '\033[1m'
verde = '\033[92m'
ciano = '\033[96m'

''' Exercício 95 - Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador. '''

time = list()
gols = list()
jogador = dict()

while True:
    while True:
        jogador['Nome'] = str(input(f'{limpar}Nome do jogador:{verde} '))
        if jogador['Nome'].replace(' ', '').isalpha() == False:
            print(f'{limpar}Nomes só podem ter caracteres alfabéticos. Tente novamente!')
        else:
            break
    partidas = int(input(f'{limpar}Quantas partidas {jogador['Nome']} jogou?{verde} '))
    if partidas == 0:
        jogador['Gols'] = []
        jogador['Total de gols'] = 0
        time.append(jogador.copy())
    elif partidas < 0:
        print(f'{limpar}Por favor, insira um número positivo ou 0!')
    else:
        for c in range(0, partidas):
            gols.append(int(input(f'{limpar}{'- ':>4}Gols feitos na {c+1}ª partida:{verde} ')))
            total_gols = sum(gols) # ou 'total_gols += gols[c]' dentro de 'for' acima.
            jogador['Gols'] = gols[:]
            jogador['Total de gols'] = total_gols
        time.append(jogador.copy())
        gols.clear()
    while True:
        continuar = str(input(f'\n{limpar}Deseja continuar? [S/N]{verde} ').strip()[0])
        if continuar not in 'SsNn':
            print(f'{limpar}Resposta inválida, tente novamente!')
        else:
            break
    if continuar in 'Nn':
        break
print(f'{limpar}'+'~~~~'*20)
print(f'{negrito}{'ID':<3}{limpar}', end=' ')
for chave in jogador.keys():
    print(f'{negrito}{chave:<15}{limpar}', end ='')
print('\n'+20*'~~~~')
for pos, dicionário in enumerate(time):
    print(f'{pos:<3}', end=' ')
    for valor in dicionário.values():
        print(f'{str(valor):<15}',end='')
    print()
print(20*'~~~~')
while True:
    id = int(input(f'{limpar}Mostrar dados de qual jogador? [999 para sair]{verde} '))
    if id == 999:
        break
    elif id < 0 or id >= len(time):
        print(f'{limpar}ID inválido, tente novamente!')
    else:
        print(f'{limpar}-- O jogador {negrito}{time[id]['Nome']}{limpar} jogou {ciano}{len(time[id]['Gols'])}{limpar} partidas! --')
        for pos, valor in enumerate(time[id]['Gols']):
            print(f'{'=> ':>10}{negrito}{pos+1}ª{limpar} partida: {ciano}{valor}{limpar} gols <=')
    print(20*'~~~')
print(f'{limpar}--- ATÉ LOGO! ---')
