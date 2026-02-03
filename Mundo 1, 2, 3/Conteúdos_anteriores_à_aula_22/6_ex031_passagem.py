# Dicionário de cores
cores = {
    'LIMPAR': '\033[m',
    'VERDE': '\033[92m',
    'CIANO': '\033[96m'
}

''' Exercício 31 - Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas. '''

distancia_viagem = float(input(f'Digite a distância da sua viagem em KM:{cores['VERDE']} ')) 
print(cores['LIMPAR'])

if distancia_viagem <= 200:
   preco = distancia_viagem * 0.50
else:
   preco = distancia_viagem * 0.45
print(f'O preço da passagem será de {cores['CIANO']}R${preco:.2f}{cores['LIMPAR']}\n')

# Forma mais concisa, porém menos recomendada.
preco = distancia_viagem * 0.50 if distancia_viagem <= 200 else distancia_viagem * 0.45
print(f'O preço da passagem será de {cores['CIANO']}R${preco:.2f}{cores['LIMPAR']}')
