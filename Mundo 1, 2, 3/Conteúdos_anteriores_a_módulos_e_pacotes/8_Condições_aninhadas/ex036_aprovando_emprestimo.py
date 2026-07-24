# Variáveis de cores
limpar = '\033[m'
vermelho = '\033[91m'
verde = '\033[92m'
ciano = '\033[96m'

''' Exercício 36 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado. '''

valor = float(input(f'Insira o valor da casa: {verde}R$'))
salario = float(input(f'{limpar}Insira o seu salário: {verde}R$'))
tempo = int(input(f'{limpar}Em quantos anos você quer pagar?{verde} '))
print(limpar)
prestacao = valor / (tempo * 12)

print(f'Para pagar o valor de R${valor} do imóvel em {tempo} anos, a prestação será de {prestacao:.2f}\n')

if prestacao > (salario * 0.30):
 print(f'A prestação excede o limite de 30% do seu salário, ou seja, o emprestimo foi {vermelho}NEGADO!{limpar}.')
else:
 print(f'Parabéns, seu empréstimo foi {ciano}APROVADO!{limpar}')
