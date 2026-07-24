# Variáveis de cores
limpar = '\033[m'
negrito = '\033[1m'
verde = '\033[92m'

''' Exercício 43 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida '''

peso = float(input(f'Digite seu peso:{verde} (KG) '))
altura = float(input(f'{limpar}Digite sua altura:{verde} (m) '))
print(limpar)
imc = peso / (altura**2)

print(f'Seu IMC é {imc:.1f}, ou seja, você está com',end=' ')

if imc < 18.5:
    print(f'{negrito}magreza{limpar}.')
elif imc <= 25:
    print(f'{negrito}peso ideal{limpar}.')
elif imc <= 30:
    print(f'{negrito}sobrepreso{limpar}.')
elif imc <= 40:
    print(f'{negrito}obesidade{limpar}.')
else:
    print(f'{negrito}obesidade mórbida{limpar}.')
