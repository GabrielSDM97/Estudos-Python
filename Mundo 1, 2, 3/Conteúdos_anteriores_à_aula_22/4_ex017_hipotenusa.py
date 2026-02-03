from math import hypot

''' Exercício 17 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
Calcule e mostre o comprimento da hipotenusa. '''

catetox = float(input('Insira o valor do cateto oposto:\033[92m '))
catetoy = float(input('\033[mInsira o valor do cateto adjacente:\033[92m '))

print('\033[m')
print(f'A hipotenusa vai medir \033[96m{hypot(catetox, catetoy):.2f}.\033[m')