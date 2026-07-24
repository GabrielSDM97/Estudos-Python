''' Exercício 26 - Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", 
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

Obs.: A primeira posição não pode ser 0. '''

frase = str(input('Digite uma frase:\033[92m ').strip().upper().replace('Á', 'A').replace('À', 'A').replace('Â', 'A').replace('Ã', 'A'))
print('\033[m')

print(f'A letra A aparece \033[96m{frase.count('A')}\033[m vezes.\n')
print(f'A primeira letra "A" aparece na posição \033[96m{frase.find('A')+1}\033[m.\n')
print(f'A última letra "A" aparece na posição \033[96m{frase.rfind('A')+1}\033[m.\n')
