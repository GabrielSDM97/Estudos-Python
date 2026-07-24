''' Exercício 14 - Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit. '''

celsius = float(input('Insira uma temperatura em Cº:\033[92m '))

print('\033[m')
print(f'A temperatura de {celsius}Cº corresponde a {((celsius * 9/5) + 32):.1f}Fº.')