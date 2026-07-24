# Variáveis de cores
limpar = '\033[m'
vermelho = '\033[91m'
verde = '\033[92m'

''' Exercício 83 - Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta. '''

# Minha resolução

expressão = str(input(f'Digite a expressão:{verde} '))
p_aberto = p_fechado = 0

for pos, caractere in enumerate(expressão):
    if p_aberto < p_fechado:
        break
    else:
        if caractere == '(' in expressão:
            p_aberto += 1
        elif caractere == ')' in expressão:
            p_fechado += 1
if (p_aberto != p_fechado) or (p_aberto < p_fechado):
    print(f'{limpar}Expressão {vermelho}incorreta{limpar}!')
else:
    print(f'{limpar}Expressão {verde}correta{limpar}!')


''' Resolução do Guanabara.

expressão = str(input(f'Digite a expressão:{verde} '))
pilha = []

for caractere in expressão:
    if caractere == '(':
        pilha.append('(')
    elif caractere == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append('(')
            break
if len(pilha) == 0:
    print(f'{limpar}Expressão {verde}correta{limpar}!')
else:
    print(f'{limpar}Expressão {vermelho}incorreta{limpar}!')

'''