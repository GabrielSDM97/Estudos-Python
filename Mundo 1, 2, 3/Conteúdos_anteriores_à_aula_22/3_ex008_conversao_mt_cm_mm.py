''' Exercício 8 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros. '''

m = float(input("Digite uma distância em metros: "))

print(f'{m}m equivale a:')
print(f'\033[32m{(m * 100):.0f}cm.\033[m') 
print(f'\033[33m{(m * 1000):.0f}mm.\033[m')
