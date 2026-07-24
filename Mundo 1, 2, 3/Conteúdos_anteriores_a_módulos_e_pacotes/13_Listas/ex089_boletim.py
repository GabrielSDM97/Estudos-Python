# Variáveis de cores
limpar = '\033[m'
negrito = '\033[1m'
verde = '\033[92m'
amarelo = '\033[93m'
ciano = '\033[96m'

''' Exercício 89 - Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente. '''

boletins = list()
id = 0

while True:
    nome = str(input(f'\n{limpar}Nome:{verde} '))
    nota1 = float(input(f'{limpar}Nota 1:{verde} '))
    nota2 = float(input(f'{limpar}Nota 2:{verde} '))
    media = (nota1+nota2)/2
    boletins.append([nome, [nota1, nota2], media])
    continuar = str(input(f'\n{limpar}Quer cadastrar mais um aluno? [S/N]{verde} '))
    if continuar in 'Nn':
        break
print(limpar)
print(25*'~')
print(f'{negrito}{'ID':<7}{'Nome':<11}{'Média'}{limpar}')
for c in range(0,len(boletins)):
    print(f'{c:<7}{boletins[c][0]:<11}{boletins[c][2]}')
print(25*'~')
while True:
    id_aluno = int(input('\nInsira o ID do aluno cujas notas você quer ver [999 para sair]: '))
    if id_aluno == 999:
        break
    for pos in range(0,len(boletins)):
        if id_aluno == pos:
            print(f'Notas do aluno {amarelo}{boletins[id_aluno][0]}{limpar}: {ciano}{boletins[id_aluno][1]}{limpar}')
            break
        elif pos == len(boletins)-1:
            print('ID inválido, tente novamente!')
print('~~~ Até logo! ~~~')
