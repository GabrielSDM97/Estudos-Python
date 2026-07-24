''' Exercício 48 - Faça um programa que calcule a soma entre todos os números que são ímpares e múltiplos de três que se encontram no intervalo de 1 até 500. '''

soma_impar = contador_impar = 0

for contador in range(3,496,3):
    if contador % 2 == 1:
        contador_impar += 1
        soma_impar += contador
print(f'A soma dos {contador_impar} números ímpares e múltiplos de 3 é {soma_impar}.')
