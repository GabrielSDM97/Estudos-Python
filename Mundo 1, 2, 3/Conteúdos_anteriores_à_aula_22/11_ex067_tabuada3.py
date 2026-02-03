# Variáveis de cores
limpar = '\033[m'
verde = '\033[92m'
ciano = '\033[96m'

''' Exercício 67 - Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo. '''

while True:
    multiplicando = int(input(f'{limpar}Você quer uma tabuada de qual valor? [número negativo para sair]:{verde} '))
    if multiplicando < 0:
        break
    print(20*f'{limpar}~',f'Tabuada de {ciano}{multiplicando}{limpar}',20*'~')
    for multiplicador in range(1, 11):
        print(f'{multiplicando} x {multiplicador:2} = {multiplicando * multiplicador}')
    print(55*'~')
print(f'\n{limpar}Até logo!')
