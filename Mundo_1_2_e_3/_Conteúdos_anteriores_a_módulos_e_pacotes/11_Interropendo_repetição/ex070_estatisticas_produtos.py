# Variáveis de cores
limpar = '\033[m'
verde = '\033[92m'
amarelo = '\033[93m'
ciano = '\033[96m'

''' Exercício 70 - Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''

contador = contador_1000 = valor_total = 0

while True:
    print(limpar)
    print(20*f'=',f'\n{'Cadastro de produto':^20}')
    print(20*'=')
    contador += 1
    nome = str(input(f'\n{limpar}Nome do produto:{verde} ').strip().capitalize())
    preço = float(input(f'{limpar}Preço do produto:{verde} R$'))
    valor_total += preço
    if contador == 1 or preço < produto_barato:
        produto_barato = preço
        nome_barato = nome
    if preço > 1000:
        contador_1000 += 1
    print(f'\n{amarelo}Produto cadastrado com sucesso!{limpar}')
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input(f'\n{limpar}Deseja cadastrar mais um produto? [S/N]{verde} ').strip()[0])
        if continuar not in 'SsNn':
            print(f'{limpar}Resposta inválida, tente novamente!')
    if continuar in 'Nn':
        break
print(limpar)
print(10*'~','Análise geral de dados cadastrados',10*'~')
print(f"""A) Total gasto na compra. {ciano}R${valor_total}{limpar}
B) Produtos que custam mais de R$1000: {ciano}{contador_1000}{limpar}
C) Nome do produto mais barato: {ciano}{nome_barato}{limpar}\n""")
