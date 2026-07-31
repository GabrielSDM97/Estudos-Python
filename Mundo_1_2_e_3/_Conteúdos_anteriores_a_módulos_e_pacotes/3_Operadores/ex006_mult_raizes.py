''' Exercício 6 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada. '''

num = float(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raizq = num**(1/2)

print(f'\nO dobro de {num} é \033[92m{dobro}\033[m\n')
print(f'O triplo de {num} é \033[92m{triplo}\033[m.\n')
print(f'A raiz quadrada de {num} é \033[92m{raizq:.2f}\033[m\n')
print(20*'\033[96m-=-\033[m')

# Forma mais concisa de fazer utilizando apenas uma variável e incluindo os calculos nas máscaras.
print(f'\nO dobro de {num} é \033[92m{num * 2}\033[m\n')
print(f'O triplo de {num} é \033[92m{num * 3}\033[m.\n')
print(f'A raiz quadrada de {num} é \033[92m{num**(1/2):.2f}\033[m\n')
