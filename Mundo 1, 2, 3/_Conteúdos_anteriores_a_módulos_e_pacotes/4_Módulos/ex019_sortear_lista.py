from random import choice

''' Exercício 19 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido. '''

aluno1 = str(input('Digite o nome do primeiro aluno:\033[92m '))
aluno2 = str(input('\033[mDigite o nome do segundo aluno:\033[92m '))
aluno3 = str(input('\033[mDigite o nome do terceiro aluno:\033[92m '))
aluno4 = str(input('\033[mDigite o nome do quarto aluno:\033[92m '))
print('\033[m')
# Listas ficam entre colchetes "[]".
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(lista)

print(f'O aluno escolhido foi {escolhido}')