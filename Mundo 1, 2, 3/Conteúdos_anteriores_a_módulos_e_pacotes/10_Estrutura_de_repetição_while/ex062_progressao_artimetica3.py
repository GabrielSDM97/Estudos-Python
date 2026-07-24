# Variáveis de cores
limpar = '\033[m'
verde = '\033[92m'
ciano = '\033[96m'

''' Exercício 62 -  Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerrará quando ele disser que quer mostrar 0 termos. '''

primeiro_termo = int(input(f'Primeiro termo:{verde} '))
razao = int(input(f'{limpar}Razão:{verde} '))
print(limpar)
termos = 10
soma_termos = 0
contador = 0

while termos != 0:
    soma_termos += termos
    while contador < soma_termos:
        proximo_termo = primeiro_termo + contador * razao
        print(f'{ciano}{proximo_termo}{limpar} {'→ FIM!\n' if contador == soma_termos-1 else '→' }',end=' ')
        contador += 1
    termos = int(input(f'\nQuantos termos a mais você quer ver? [0 para sair] \nDigite aqui:{verde} '))
    print(limpar)
print('Até logo!')
