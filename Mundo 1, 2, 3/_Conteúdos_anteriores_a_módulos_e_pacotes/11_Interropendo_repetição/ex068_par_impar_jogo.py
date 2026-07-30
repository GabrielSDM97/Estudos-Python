from random import randint

# Variáveis de cores
limpar = '\033[m'
negrito = '\033[1m'
vermelho = '\033[91m'
verde = '\033[92m'
ciano = '\033[96m'

''' Exercício 68 - Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.  '''

pontos = 0

while True:
    num_computador = randint(0,10)
    num_jogador = int(input(f'Diga um número de 0 a 10:{verde} '))
    escolha = str(input(f'{limpar}Par ou impar?{verde} ').strip().upper().replace('I','Í'))
    soma = num_computador + num_jogador
    if num_jogador > 10 or num_jogador < 0:
        print(f'\n{limpar}Parece que temos um alien aqui, {negrito}{vermelho}como você tem {num_jogador} dedos?????{limpar}\n')
    elif escolha != 'PAR' and escolha != 'ÍMPAR':
        print(f'\n{limpar}Escolha inválida, tente novamente!\n')
    elif escolha in 'PAR' and soma % 2 == 1 or escolha == 'ÍMPAR' and soma % 2 == 0:
        print(f'\n{limpar}Você escolheu {num_jogador} e a maquina {num_computador}, totalizando {soma}. Como você escolheu {negrito}{escolha}{limpar}, {vermelho}você perdeu{limpar}!!!\n')
        break
    else:
        print(f'\n{limpar}Você escolheu {num_jogador} e a maquina {num_computador} totalizando {soma}. Como você escolheu {negrito}{escolha}{limpar}, {ciano}você venceu{limpar}!!!\n')
        pontos += 1
print(f'Rodadas vencidas: {verde}{pontos}{limpar}\n')
