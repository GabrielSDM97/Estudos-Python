''' Exercício 24 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO". '''

cidade = str(input('Digite o nome de uma cidade:\033[92m ').strip().upper())
print('\033[m')
# Outra forma de fazer o metodo format abaixo é: ".format(cid[:5].upper() == 'SANTO'))"
print(f'Essa cidade começa com "SANTO"? \033[96m{cidade.startswith('SANTO')}\033[m')
