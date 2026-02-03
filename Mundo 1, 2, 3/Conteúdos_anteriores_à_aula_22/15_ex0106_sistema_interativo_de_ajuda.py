from time import sleep

l = '\033[m'  # Limpar

# Tuplas de cores
# Caracteres - 0 Preto, 1 Vermelho, 2 Verde, 3 Amarelo, 4 Roxo, 5 Magenta, 6 Ciano, 7 Branco.
c = ('\033[90m',
     '\033[91m',
     '\033[92m',
     '\033[93m',
     '\033[94m',
     '\033[95m',
     '\033[96m',
     '\033[97m')

# Fundo - 0 Preto, 1 Vermelho, 2 Verde, 3 Amarelo, 4 Roxo, 5 Magenta, 6 Ciano, 7 Branco.
bgc = ('\033[100m',
       '\033[101m',
       '\033[102m',
       '\033[103m',
       '\033[104m',
       '\033[105m',
       '\033[106m',
       '\033[107m')

''' Exercício 106 - Faça um mini-sistema que utilize o Interactive Help do Python. 
O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores. '''

'''
def ajuda(comando):
    com = str(input(f'{comando}').strip())
    sleep(1.5)
    if com.upper() == 'FIM':
        título('Até logo')
        quit()
    título(f'Acessando o manual do comando "{com}"', 0, 2)
    sleep(1.5)
    print(f'{c[0]}{bgc[7]}')
    help(com)
    print(l)


def título(texto, cor=0, fundo=0):
    print(f'{c[cor]}{bgc[fundo]}' + (len(texto)+4) * '~')
    print(f'  {texto}')
    print((len(texto)+4) * '~' + f'{l}')


while True:
    sleep(1)
    título('Sistema de ajuda PyHELP', 0, 6)
    fb = ajuda(f'{l}Função ou Biblioteca > {c[2]}') '''


def ajuda(comando):
    sleep(1.5)
    título(f'Acessando o manual do comando "{comando}"', 0, 2)
    sleep(1.5)
    print(f'{c[0]}{bgc[7]}')
    help(comando)
    print(l)


def título(texto, cor=0, fundo=0):
    print(f'{c[cor]}{bgc[fundo]}' + (len(texto)+4) * '~')
    print(f'  {texto}')
    print((len(texto)+4) * '~' + f'{l}')


while True:
    sleep(1)
    título('Sistema de ajuda PyHELP', 0, 6)
    fb = str(input(f'{l}Função ou Biblioteca > {c[2]}'))
    if fb.strip().upper() == 'FIM':
        título('Até logo')
        break
    else:
        ajuda(fb)
