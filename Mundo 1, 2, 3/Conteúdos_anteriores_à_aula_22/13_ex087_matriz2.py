# Variáveis de cores
limpar = '\033[m'
verde = '\033[92m'
ciano = '\033[96m'

''' Exercício 87 - Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha. '''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = soma_coluna = maior_valor = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'{limpar}Digite um valor para [{linha},{coluna}]:{verde} '))
        
        if matriz[linha][coluna] % 2 == 0: 
            soma_par += matriz[linha][coluna] # A soma de todos os valores pares digitados.
        
        soma_coluna += matriz[linha][2] # A soma dos valores da terceira coluna.
        
        if linha == 1 and coluna == 0: 
            maior_valor = matriz[linha][coluna] # Inserção do primeiro valor da segunda linha para servir como base para a condição abaixo.
        elif linha == 1 and matriz[linha][coluna] > maior_valor:  
            maior_valor = matriz[linha][coluna] # O maior valor da segunda linha.
print(limpar)
print(10*'-=-')
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{ciano}{matriz[linha][coluna]:^6}{limpar}]', end=' ')
    print()
print(10*'-=-')
print(f'Soma de todos os valores pares: {ciano}{soma_par}{limpar};\nSoma dos valores da 3ª coluna: {ciano}{soma_coluna}{limpar};\nMaior valor 2ª linha: {ciano}{maior_valor}{limpar}.')
