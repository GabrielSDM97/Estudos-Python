from datetime import date
from time import sleep
from random import choice

# Variáveis de cores
limpar = '\033[m'
negrito = '\033[1m'
vermelho = '\033[91m'
verde = '\033[92m'
ciano = '\033[96m'

''' Exercício 45 - Crie um programa que faça o computador jogar Jokenpô com você. '''

print(10*'-=','Pedra, Papel, Tesoura',10*'=-','\n')

jogador = str(input(f'Escolha entre pedra, papel ou tesoura:{verde} ').strip().lower())
print(limpar)
escolhas = ['pedra','papel','tesoura']
maquina = choice(escolhas)

print('JO 🪨')
sleep(1)
print('KEN 📄')
sleep(1)
print('PO ✂️\n')

print(f'Você escolheu {negrito}{verde}{jogador}{limpar}.')
print(f'A maquina escolheu {negrito}{vermelho}{maquina}{limpar}.\n')

if (maquina == 'pedra' and jogador == 'tesoura') or (maquina == 'papel' and jogador == 'pedra') or (maquina == 'tesoura' and jogador == 'papel'):
    print(f'{negrito}{vermelho}Máquina{limpar}: Hahaha, eu ganhei 😎\n')
elif (jogador == 'pedra' and maquina == 'tesoura') or (jogador == 'papel' and maquina == 'pedra') or (jogador == 'tesoura' and maquina == 'papel'):
    print(f'{negrito}{vermelho}Máquina{limpar}: Aff, você ganhou 😒\n')
elif (maquina == 'pedra' and jogador == 'pedra') or (maquina == 'papel' and jogador == 'papel') or (maquina == 'tesoura' and jogador == 'tesoura'):
    print(f'{negrito}{vermelho}Máquina{limpar}: Empatamos, vamos tentar novamente!\n')
else:
    print(f'{negrito}{vermelho}Máquina{limpar}: Pare de palhaçada 🤬, escolha entre pedra, papel ou tesoura!\n')

print(10*'-=',f'Processado em {date.today()}',10*'=-')
