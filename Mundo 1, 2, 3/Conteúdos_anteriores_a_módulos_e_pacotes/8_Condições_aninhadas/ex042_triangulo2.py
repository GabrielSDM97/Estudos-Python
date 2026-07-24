# Variáveis de cores
limpar = '\033[m'
negrito = '\033[1m'
vermelho = '\033[91m'
verde = '\033[92m'
ciano = '\033[96m'

''' Exercício 42 - Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes  '''

lado_a = float(input(f'Primeiro segmento:{verde} '))
lado_b = float(input(f'{limpar}Segundo segmento:{verde} '))
lado_c = float(input(f'{limpar}Terceiro segmento:{verde} '))
print(limpar)

if (lado_a + lado_b) > lado_c and (lado_a + lado_c) > lado_b and (lado_b + lado_c) > lado_a:
    print(f'Os seguimentos acima {ciano}PODEM{limpar} formar um triângulo, e o tipo deste triângulo é',end=' ')
    if lado_a == lado_b == lado_c:
        print (f'{negrito}EQUILÁTERO{limpar}.')
    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        print (f'{negrito}ISÓSCELES{limpar}.')
    else:
        print (f'{negrito}ESCALENO{limpar}.')
else:
    print(f'Os seguimentos acima {vermelho}NÃO PODEM{limpar} formar um triângulo.')
