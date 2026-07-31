# Variáveis de cores
limpar = '\033[m'
verde = '\033[92m'
ciano = '\033[96m'

''' Exercício 76 - Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados em forma tabular. '''

produtos = ('Tablet', 2000, 'Smartphone', 1500, 'PC Gamer', 7500, 'TV Smart', 5000, 'Smartwatch', 500)

print(18*'-',f'{ciano}Mercado de eletrônicos{limpar}',17*'-')
for posição in range(0,len(produtos)):
    if posição % 2 == 0:
        print(f'| Nome do produto: {produtos[posição]:<20}',end='')
    else:
        print(f'Preço: R${verde}{produtos[posição]:<10.2f}{limpar}|')
print(f'{29*'--':^60}')
