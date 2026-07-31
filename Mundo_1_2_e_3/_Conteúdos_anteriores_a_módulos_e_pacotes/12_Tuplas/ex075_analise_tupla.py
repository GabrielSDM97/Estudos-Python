# Variáveis de cores
limpar = '\033[m'
verde = '\033[92m'
ciano = '\033[96m'

''' Exercício 75 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: 
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares. '''

# É possível criar inputs em cada posição de uma tupla.
tupla = (int(input(f'Insira o 1º valor:{verde} ')),
        int(input(f'{limpar}Insira o 2º valor:{verde} ')),
        int(input(f'{limpar}Insira o 3º valor:{verde} ')),
        int(input(f'{limpar}Insira o 4º valor:{verde} ')))
print(limpar)

print('A) Quantas vezes apareceu o valor 9:',end=' ')
print(f'{ciano}{tupla.count(9)}{limpar}.')

print('B) Em que posição aparece o primeiro valor 3:',end=' ')
if 3 in tupla:
    print(f'{ciano}{tupla.index(3)+1}{limpar}.')
else:
    print(f'{ciano}O número 3 não foi digitado.{limpar}')

print('C) Os números pares foram:',end=' ')
for num in tupla:
    if num % 2 == 0:
        print(f'{ciano}{num}{limpar};',end=' ')
