''' Exercício 9 - Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada. '''

num = int(input('Insira um número para a tabuada: '))

print(f'Tabuada de {num}: ')
print(12*'\033[36m-=\033[m')
print(f'{num} x {1:2} = \033[92m{(num * 1)}\033[m')
print(f'{num} x {2:2} = \033[92m{(num * 2)}\033[m')
print(f'{num} x {3:2} = \033[92m{(num * 3)}\033[m')
print(f'{num} x {4:2} = \033[92m{(num * 4)}\033[m')
print(f'{num} x {5:2} = \033[92m{(num * 5)}\033[m')
print(f'{num} x {6:2} = \033[92m{(num * 6)}\033[m')
print(f'{num} x {7:2} = \033[92m{(num * 7)}\033[m')
print(f'{num} x {8:2} = \033[92m{(num * 8)}\033[m')
print(f'{num} x {9:2} = \033[92m{(num * 9)}\033[m')
print(f'{num} x {10} = \033[92m{(num * 10)}\033[m')
print(12*'\033[34m-=\033[m')
