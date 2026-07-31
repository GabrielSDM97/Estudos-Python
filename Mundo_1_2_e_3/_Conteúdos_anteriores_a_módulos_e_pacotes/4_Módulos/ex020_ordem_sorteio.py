from random import shuffle

''' Exercício 20 - O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. 
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada. '''

aluno1 = str(input('Digite o nome do primeiro aluno:\033[92m '))
aluno2 = str(input('\033[mDigite o nome do segundo aluno:\033[92m '))
aluno3 = str(input('\033[mDigite o nome do terceiro aluno:\033[92m '))
aluno4 = str(input('\033[mDigite o nome do quarto aluno:\033[92m '))
print('\033[m')
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)

print(f'A ordem de apresentação será {lista}')