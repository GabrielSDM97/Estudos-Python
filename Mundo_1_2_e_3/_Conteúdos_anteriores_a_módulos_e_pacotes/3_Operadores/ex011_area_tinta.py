''' Exercício 11 - Faça um programa que leia a largura e a altura de uma parede em metros, 
calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados. '''

altura = float(input('Digite a altura da parede em metros:\033[32m '))
largura = float(input('\033[mDigite a largura da parede em metros:\033[32m '))
area = altura*largura

print('\033[m')
print(f'A área de uma parede com {altura}m de altura e {largura}m de largura é {area:.2f}m²\n')
print(f'Já que é necessário 1 litro de tinta para cada 2m², para pintar {area:.2f}m² será nececessário {(area/2):.0f} litros')