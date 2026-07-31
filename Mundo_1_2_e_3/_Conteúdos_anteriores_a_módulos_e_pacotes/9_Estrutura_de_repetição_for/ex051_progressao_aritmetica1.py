# Variáveis de cores
limpar = '\033[m'
verde = '\033[92m'

''' Exercício 51 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão. '''

primeiro_termo = int(input(f'Digite o primeiro termo:{verde} '))
razao = int(input(f'{limpar}Digite a razão:{verde} '))
print(limpar)

for contador in range(0,10):
    proximo_termo = primeiro_termo + contador * razao
    print(f'{proximo_termo} →',end=' ')
print('FIM!!!')
