from math import radians, sin, cos, tan

''' Exercício 18 -  Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. 

Obs.: É necessário converter graus em radianos antes de gerar o seno, cosseno e tangente. '''

angulo = float(input('Digite um ângulo:\033[96m '))
print('\033[m') 
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'Com o ângulo {angulo} temos:\nSeno \033[92m{seno:.2f}\033[m.\nCosseno \033[92m{cosseno:.2f}\033[m.\nTangente \033[92m{tangente:.2f}\033[m.')