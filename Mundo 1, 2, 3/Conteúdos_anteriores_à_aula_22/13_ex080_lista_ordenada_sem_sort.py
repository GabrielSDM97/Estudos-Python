# Variáveis de cores
limpar = '\033[m'
verde = '\033[92m'
amarelo = '\033[93m'
ciano = '\033[96m'

''' Exercício 80 - Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). 
No final, mostre a lista ordenada na tela. '''

lista = list()
for c1 in range (5):
    valor = int(input(f'\n{limpar}Insira o {c1+1}º valor:{verde} '))
    for c2 in range(0,len(lista)): 
        if valor <= lista[c2]: # Verifica se o valor inserido é menor que todos os outros valores da lista.
            lista.insert(c2, valor)
            print(f'{limpar}Adicionado na posição {ciano}{c2}{limpar} da lista!')
            break
    # Opção 1
    if valor not in lista: # Caso não seja identificado nenhum valor igual ou maior na lista,...
        lista.append(valor) #... o valor atual será inserido no fim da lista como o maior até o momento.
        print(f'{limpar}Adicionado na última posição da lista!')
    # Opção 2
    ''' if c1 == 0 or valor > lista[-1]:
            lista.append(valor)
            print(f'{limpar}Adicionado na última posição da lista!') '''
print(f'\nNúmeros da lista em ordem: {amarelo}{lista}{limpar}.')

'''  
# Utilizando a biblioteca "bisect"

from bisect import insort

lista = list()

for c in range(5):

    valor = int(input('Insira um valor: '))

    insort(lista, valor) # Já insere 'n' na lista de forma ordenada:

    print(f'Número {valor} incluido na posição {lista.index(valor)}.')

print(f'Números da lista em ordem: {lista}') '''
