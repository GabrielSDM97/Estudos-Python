# Variáveis de cores
limpar = '\033[m'
negrito = '\033[1m'
verde = '\033[92m'
amarelo = '\033[93m'
ciano = '\033[96m'

''' Exercício 53 - Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. 

Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA. '''

frase = str(input(f'Digite uma frase:{verde} ').upper().replace(' ', ''))
print(limpar)
contrario = ''

for contador in range(len(frase)-1,-1,-1):
    contrario += frase[contador]
if frase == contrario:
    print(f'O inverso de {negrito}{frase}{limpar} é {negrito}{contrario}{limpar}. {ciano}São palíndromos{limpar}.')
else:
    print(f'O inverso de {negrito}{frase}{limpar} é {negrito}{contrario}{limpar}. {amarelo}Não são palíndromos{limpar}.')
