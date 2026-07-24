# Variáveis de cores
limpar = '\033[m'
vermelho = '\033[91m'
verde = '\033[92m'
amarelo = '\033[93m'

''' Exercício 90 - Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela. '''

aluno = dict()
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = float(input(f'Insira a média do aluno {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situação'] =  f'{verde}Aprovado{limpar}'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = f'{amarelo}Recuperação{limpar}'
else:
    aluno['situação'] = f'{vermelho}Reprovado{limpar}'

print(18*'~~')
print(f'{' ':>6} Nome do aluno: {aluno["nome"]}\n{' ':>6} Media: {aluno['media']}\n{' ':>6} Situação: {aluno["situação"]}')
print(18*'~~')
