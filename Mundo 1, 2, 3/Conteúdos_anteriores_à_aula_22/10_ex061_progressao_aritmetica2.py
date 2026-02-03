# Variáveis de cores
limpar = '\033[m'
verde = '\033[92m'
ciano = '\033[96m'

''' Exercício 61 -  Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while. '''

primeiro_termo = int(input(f'Primeiro termo:{verde} '))
razao = int(input(f'{limpar}Razão:{verde} '))
print(limpar)
contador = 0

while contador < 10:
    proximo_termo = primeiro_termo + contador * razao
    print(f'{ciano}{proximo_termo}{limpar} →',end=' ')
    contador += 1
print('FIM!')
