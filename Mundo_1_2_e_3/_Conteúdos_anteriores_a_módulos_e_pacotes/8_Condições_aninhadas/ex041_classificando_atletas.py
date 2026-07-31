from datetime import date

# Variáveis de cores
limpar = '\033[m'
negrito = '\033[1m'
verde = '\033[92m'

''' Exercício 41 - A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER '''

ano_nascimento = int(input(f'Digite o seu ano de nascimento:{verde} '))
print(limpar)
idade = date.today().year - ano_nascimento

print(f'Você tem {idade} anos, ou seja, sua categoria deve ser',end=' ')

if idade <= 9:
    print(f'{negrito}MIRIM{limpar}.')
elif idade <= 14:
    print(f'{negrito}INFANTIL{limpar}.')
elif idade <= 19:
    print(f'{negrito}JÚNIOR{limpar}.')
elif idade <= 25:
    print(f'{negrito}SÊNIOR{limpar}.')
elif idade > 25:
    print(f'{negrito}MASTER{limpar}.')
