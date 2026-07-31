from time import sleep

''' Exercício 98 - Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. 
Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada

'''

def contador(início, fim, passo):
    if passo == 0:
        print('Passo inválido. O passo deve ser um número negativo ou positivo.')
        quit()
    print(f'\n\nDe {início} até {fim} (de {passo} em {passo}):')
    if início > fim:
        passo *= -1
    for c in range(início, fim+passo, passo):
        print(c, end=' ', flush=True)
        sleep(0.15)


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print()
contador(int(input('\nInício: ')), int(input('Fim: ')), int(input('Passo: ')))
