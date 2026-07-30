# Variáveis de cores
limpar = '\033[m'
verde = '\033[92m'
magenta = '\033[94m'
ciano = '\033[96m'

''' Exercício 49 - Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for. '''

multiplicador = int(input(f'Insira o multiplicador:{verde} '))
linhas = int(input(f'{limpar}Quantas linhas deverá ter essa tabuada?{verde} '))
print(limpar)

print(9*f'{ciano}-={limpar}',f'Tabuada de {multiplicador}', 8*f'{ciano}=-{limpar}')

for contador in range(1, linhas+1):
    print(f'{multiplicador} x {contador:2} = {verde}{multiplicador * contador}{limpar}')
print(17*f'{magenta}-=-{limpar}')
