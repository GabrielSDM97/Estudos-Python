from datetime import date

# Dicionário de cores
cores = {
    'LIMPAR': '\033[m',
    'VERMELHO': '\033[91m',
    'VERDE': '\033[92m',
    'MAGENTA': '\033[95m',
    'CIANO': '\033[96m'
}

''' Exercício 32 - Faça um programa que leia um ano qualquer e mostre se ele é bissexto. '''

ano = int(input(f'Insira um ano para saber se ele é bissexto ou não:{cores['VERDE']} '))
print(cores['LIMPAR'])

if ano == 0:
   ano = date.today().year

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f'\nO ano {ano} {cores['CIANO']}é bissexto{cores['LIMPAR']}.')
        else:
            print(f'\nO ano {ano} {cores['VERMELHO']}não é bissexto{cores['LIMPAR']}.')
    else:
        print(f'\nO ano {ano} {cores['CIANO']}é bissexto{cores['LIMPAR']}.')
else:
    print(f'\nO ano {ano} {cores['VERMELHO']}não é bissexto{cores['LIMPAR']}.')
print(27*f'{cores['MAGENTA']}-=', f'{cores['LIMPAR']}')

# Outra forma de fazer
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\nO ano {ano} {cores['CIANO']}é bissexto{cores['LIMPAR']}.')
else:
    print(f'\nO ano {ano} {cores['VERMELHO']}não é bissexto{cores['LIMPAR']}.')
print(12*f'{cores['MAGENTA']}-=', f'{cores['LIMPAR']}FIM!', 12*f'{cores['MAGENTA']}=-', f'{cores['LIMPAR']}')
