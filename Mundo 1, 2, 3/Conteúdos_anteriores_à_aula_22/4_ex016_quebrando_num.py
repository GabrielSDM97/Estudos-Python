from math import trunc

''' Exercício 16 - Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira. ''' 

num = float(input('Digite um número real:\033[92m '))

print('\033[m')
print(f'A porção inteira do número real {num} é \033[96m{trunc(num)}\033[m.')

''' Outras maneiras de fazer esse mesmo exercício

`print(f'A porção inteira do número real {num} é {num:.0f}.')`

`print(f'A porção inteira do número real {num} é {int(num)}.')`

A função 'int()' é built-in, ou seja, não necessita de nenhuma biblioteca. '''