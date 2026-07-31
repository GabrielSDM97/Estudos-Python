# Variáveis de cores
limpar = '\033[m'
verde = '\033[92m'

''' Exercício 57 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
Caso esteja errado, peça a digitação novamente até ter um valor correto. '''

sexo = str(input(f'Digite o seu sexo [M/F]:{verde} ').strip()[0])
print(limpar)

while sexo not in ('MFmf'):
    print('Dados inválidos, por favor, insira seu sexo!')
    sexo = str(input(f'Digite o seu sexo [M/F]:{verde} ').strip()[0])
    print(limpar)
if sexo in ('Mm'):
    print(f'Sexo masculino cadastrado com sucesso!!!')
else:
    print(f'Sexo feminino cadastrado com sucesso!!!')
