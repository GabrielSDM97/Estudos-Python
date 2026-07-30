''' Exercício 15 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado. '''

dias_aluguel = int(input('Por quantos dias o motorista alugou o veículo?\033[92m '))
km_rodados = float(input('\033[mQuanto KM foram rodados?\033[92m '))

print('\033[m')
print(f'O preço a ser pago é de \033[31mR${((60 * dias_aluguel) * (0.15 * km_rodados)):.2f}\033[m')
