''' Exercício 7 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média. '''

nome = str(input('Digite o nome do aluno: '))
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

print(f'O aluno {nome} finalizou com a média \033[92m{(nota1 + nota2) / 2:.1f}\033[m.')
