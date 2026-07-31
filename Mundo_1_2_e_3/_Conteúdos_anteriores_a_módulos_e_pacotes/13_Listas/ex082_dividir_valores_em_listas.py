# Variáveis de cores
limpar = '\033[m'
verde = '\033[92m'
ciano = '\033[96m'

''' Exercício 82 - Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas. '''

lista_valores = list()
lista_pares = list()
lista_impares = list()

while True:
    lista_valores.append(int(input(f'\n{limpar}Digite um valor:{verde} ')))
    continuar = str(input(f'{limpar}Deseja inserir mais um valor? [S/N]{verde} ').strip()[0])
    if continuar in 'Nn':
        break 
for valor in lista_valores:
    if valor % 2 == 0:
        lista_pares.append(valor)
    else:
        lista_impares.append(valor)
print(f'\n{limpar}Lista completa: {ciano}{sorted(lista_valores)}{limpar}\nLista par: {ciano}{sorted(lista_pares)}{limpar}\nLista ímpar: {ciano}{sorted(lista_impares)}{limpar}')
