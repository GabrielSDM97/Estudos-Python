''' Exercício 96 - Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno. '''

def area(largura, comprimento):
    área = largura * comprimento
    print(f'\nÁrea = {área}m²')


# Programa principal
area(float(input('Largura: ')), float(input('Comprimento: ')))
