# Variáveis de cores
limpar = '\033[m'
verde = '\033[92m'
amarelo = '\033[93m'
ciano = '\033[96m'

''' Exercício 84 - Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves. '''

# Minha resolução

# Na minha resolução, a verificação do maior e menor peso ocorre no 'for' depois que a lista já está feita, ou seja, após o 'while True'.

cadastro_temp = []
cadastro = []

while True:
    cadastro_temp.append(str(input(f'{limpar}Digite o seu nome:{verde} ')))
    cadastro_temp.append(float(input(f'{limpar}Digite seu peso:{verde} ')))
    cadastro.append(cadastro_temp[:])
    continuar = str(input(f'\n{limpar}Deseja cadastrar mais uma pessoa? [S/N]{verde} '))
    cadastro_temp.clear()
    if continuar in 'Nn':
        break
print(f'\n{limpar}Foram cadastradas {ciano}{len(cadastro)}{limpar} pessoas.')

maior = menor = 0

for pos, peso in enumerate(cadastro):
    if pos == 0:
        maior = menor = peso[1]
    elif peso[1] > maior :
        maior = peso[1]
    elif peso[1] < menor:
        menor = peso[1]
print(f'O maior peso registrado foi o de {ciano}{maior}Kg{limpar}. As pessoas com esse peso são: ',end='')
for peso in cadastro:
    if peso[1] == maior:
        print(f'{amarelo}{peso[0]}{limpar};', end=' ')
print(f'\nO menor peso registrado foi o de {ciano}{menor}Kg{limpar}. As pessoas com esse peso são: ',end='')
for peso in cadastro:
    if peso[1] == menor:
        print(f'{amarelo}{peso[0]}{limpar};', end= ' ')

'''

# Resolução do Guanabara

# Já na resolução do professor, a verificação do maior e menor peso ocorre dentro do 'while True' a cada novo valor inserido.

cadastro_temp = []
cadastro = []
maior = menor = 0

while True:
    cadastro_temp.append(str(input('Digite o seu nome: ')))
    cadastro_temp.append(float(input('Digite seu peso: ')))
    if len(cadastro) == 0:
        maior = menor = cadastro_temp[1]
    elif cadastro_temp[1] > maior :
        maior = cadastro_temp[1]
    elif cadastro_temp[1] < menor:
        menor = cadastro_temp[1]
    cadastro.append(cadastro_temp[:])
    continuar = str(input('\nDeseja cadastrar mais uma pessoa? [S/N] '))
    cadastro_temp.clear()
    if continuar in 'Nn':
        break
print(cadastro)
print(f'\nForam cadastradas {len(cadastro)} pessoas.')
print(f'O maior peso registrado foi o de {maior}Kg. As pessoas com esse peso são: ',end='')
for peso in cadastro:
    if peso[1] == maior:
        print(f'{peso[0]}',end=' ')
print(f'\nO menor peso registrado foi o de {menor}Kg. As pessoas com esse peso são: ',end='')
for peso in cadastro:
    if peso[1] == menor:
        print(f'{peso[0]}',end= ' ') '''
