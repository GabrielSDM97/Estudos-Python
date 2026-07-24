''' Exercício 103 - Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente. '''

def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

# Minha Resolução
''' jogador = str(input('Nome: ').strip())
t_gols = str(input('Gols: ').strip())
if jogador != '' and t_gols.isnumeric():
    ficha(jogador, int(t_gols))
elif jogador != '' and (t_gols.isalpha() or t_gols.isalnum() or t_gols == ''):
    ficha(jogador)
elif jogador == '' and t_gols.isnumeric():
    ficha(gols=int(t_gols))
elif jogador == '' and (t_gols.isalpha() or t_gols.isalnum() or t_gols == ''):
    ficha() '''

# Resolução do Guanabara
jogador = str(input('Nome: '))
t_gols = str(input('Gols: '))

if t_gols.isnumeric():
    int(t_gols)
else:
    t_gols = 0
if jogador.strip() == '':
    ficha(gols=t_gols)
else:
    ficha(jogador, t_gols)
