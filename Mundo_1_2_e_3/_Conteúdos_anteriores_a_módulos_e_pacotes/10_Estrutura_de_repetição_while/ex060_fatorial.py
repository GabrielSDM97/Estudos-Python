# Variáveis de cores
limpar = '\033[m'
verde = '\033[92m'
ciano = '\033[96m'

''' Exercício 60 - Faça um programa que leia um número qualquer e mostre o seu fatorial. '''
 
resultado = num = int(input(f'Número:{verde} '))
print(f'{limpar}')

print(f'Calculando fatorial de {num}!',end=f' = {num} x ')
while num > 1:
    num -= 1
    resultado *= num
    print(f'{num}{' x' if num != 1 else f' = {ciano}{resultado}{limpar}'}',end=' ')

# É possível tambem utilizando a função 'factorial()' da biblioteca 'math'
