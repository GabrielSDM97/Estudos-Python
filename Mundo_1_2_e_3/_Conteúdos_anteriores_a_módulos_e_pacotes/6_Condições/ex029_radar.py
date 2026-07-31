from time import sleep

''' Exercício 29 - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
A multa vai custar R$7,00 por cada Km acima do limite. '''

velocidade = int(input('Digite a velocidade do veículo:\033[92m '))
print('\033[m\nAnalisando a velocidade do veículo...\n')
sleep(2)

print(f'Sua velocidade detectada foi de {velocidade}KM/H.',end=' ')
if velocidade > 80:
    print(f'Você foi mutado em \033[91mR${(velocidade - 80) * 7}\033[m!!!')
else:
    print('Continue dirijindo com segurança!')
