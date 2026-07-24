from datetime import date

# Variáveis de cores
limpar = '\033[m'
negrito = '\033[1m'
verde = '\033[92m'
ciano = '\033[96m'

''' Exercício 92 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar. '''

cadastro = dict()
for c in range(1):
    cadastro['Nome'] = str(input(f'Nome:{verde} '))
    nascimento = int(input(f'{limpar}Ano de Nascimento:{verde} '))
    cadastro['Idade'] = date.today().year - nascimento
    cadastro['CTPS'] = int(input(f'{limpar}Carteira de trabalho [0 nao tem]:{verde} '))
    if cadastro['CTPS'] == 0:
        break
    cadastro['Contratação'] = int(input(f'{limpar}Ano de contratação:{verde} '))
    cadastro['Salário'] = float(input(f'{limpar}Salário: {verde}R$'))
    cadastro['Aposentadoria'] = (35 - (date.today().year - cadastro['Contratação'])) + cadastro['Idade']
print(f'{limpar}\n'+'~~~'*12)
for chave, valor in cadastro.items():
    print(f'{limpar}{' - ':>6}{negrito}{chave}{limpar} tem o valor {ciano}{valor}{limpar}')
print(f'~~~'*12)
