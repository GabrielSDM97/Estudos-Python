# Variáveis de cores
limpar = '\033[m'
verde = '\033[92m'
amarelo = '\033[93m'
ciano = '\033[96m'

''' Exercício 85 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente. '''

num_temp = []
lista_par_impar = [[], []]

for i in range(0, 7):
    num_temp.append(int(input(f'{limpar}Digite um valor inteiro:{verde} ')))
    if num_temp[0] % 2 == 0:
        lista_par_impar[0].append(num_temp[0])
    else:
        lista_par_impar[1].append(num_temp[0])
    num_temp.clear()
print(f'\n{limpar}Números pares: {ciano}{sorted(lista_par_impar[0])}{limpar}\nNúmeros ímpares: {amarelo}{sorted(lista_par_impar[1])}{limpar}')
