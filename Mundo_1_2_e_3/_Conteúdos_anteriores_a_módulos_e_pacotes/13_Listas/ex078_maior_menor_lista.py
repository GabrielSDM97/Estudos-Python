# Variáveis de cores
limpar = '\033[m'
verde = '\033[92m'
amarelo = '\033[93m'
ciano = '\033[96m'

''' Exercício 78 - Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.  '''

lista = [] # ou 'lista = list()'
cont_maior = 0

for contador in range(0, 6):
    lista.append(int(input(f'{limpar}Digite o {contador + 1}º valor:{verde} ')))
    if contador == 0:
        maior = menor = lista[contador]
    else:
        if lista[contador] > maior:
            maior = lista[contador]
        elif lista[contador] < menor:
            menor = lista[contador]

print(f'\n{limpar}Maior valor: {maior}')
print(f'Posição: ',end ='')
for contador in range(0,len(lista)):
    print(f'{contador}... ' if maior == lista[contador] else '',end='') # Mostra posições do maior valor.

print(f'\nMenor valor: {menor}')
print(f'Posição: ',end ='')
for contador in range(0,len(lista)):
    print(f'{contador}... ' if menor == lista[contador] else '',end='') # Mostra posições do menor valor.
