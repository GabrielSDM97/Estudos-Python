from random import randint

# Variáveis de cores
limpar = '\033[m'
verde = '\033[92m'
ciano = '\033[96m'

''' Exercício 74 - Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla. '''

tupla = (randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))
print(f'Valores sorteados:',end=' ')
for n in tupla:
    print(f'{verde}{n}{limpar}',end=' ')

# Opção 1
''' for pos, c in enumerate(tupla):
    if pos == 0:
        maior = menor = tupla[0]
    else:
        if tupla[pos] > maior:
            maior = tupla[pos]
        if tupla[pos] < menor:
            menor = tupla[pos]
print(f'Maior {maior}. Menor {menor}.') '''

# Opção 2
# print(f'\nMaior valor: {ciano}{sorted(tupla)[-1]}{limpar}. Menor valor: {ciano}{sorted(tupla)[0]}{limpar}.')
      
# Opção 3 (Mais eficiente)
print(f'\nMaior valor: {ciano}{max(tupla)}{limpar}. Menor valor: {ciano}{min(tupla)}{limpar}.')
