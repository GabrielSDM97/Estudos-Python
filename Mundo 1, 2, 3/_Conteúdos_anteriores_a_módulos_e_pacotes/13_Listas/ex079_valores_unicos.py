# Variáveis de cores
limpar = '\033[m'
verde = '\033[92m'
ciano = '\033[96m'

''' Exercício 79 - Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. '''

lista = list()

while True:
    valor = int(input(f'{limpar}Insira um valor:{verde} '))
    if valor in lista:
        print(f'{limpar}O valor {ciano}{valor}{limpar} já está na lista, tente outro número!\n')
    else:
        lista.append(valor)
        print(f'{limpar}Valor {ciano}{valor}{limpar} cadastrado com sucesso!\n')
    while True:
        continuar = str(input(f'{limpar}Quer continuar? [S/N] {verde}').strip()[0])
        if continuar not in 'SsNn':
            print(f'{limpar}Resposta inválida, tente novamente!')
        else:
            break
    if continuar in 'Nn':
        break
lista.sort()
print(f'{limpar}Lista em ordem crescente: {lista}\n',end=' ')
