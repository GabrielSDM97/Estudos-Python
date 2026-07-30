# Variáveis de cores
limpar = '\033[m'
vermelho = '\033[91m'
verde = '\033[92m'
amarelo = '\033[93m'
ciano = '\033[96m'

''' Exercício 40 - Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO '''

nota1 = float(input(f'Digite sua primeira nota:{verde} '))
nota2 = float(input(f'{limpar}Digite sua segunda nota:{verde} '))
print(limpar)
media = (nota1 + nota2)/2

print(f'Você tirou {nota1} e {nota2}, ou seja, ficou com média {media:.1f}\n')

if media < 5:
    print(f'Você está {vermelho}REPROVADO!!!{limpar}')
elif 7 > media >= 5: # Equivale a = 'elif media >= 5 and media < 7:'
    print(f'Você está de {amarelo}RECUPERAÇÃO!!!{limpar}')
else:
    print(f'Você está {ciano}APROVADO!!!{limpar}')