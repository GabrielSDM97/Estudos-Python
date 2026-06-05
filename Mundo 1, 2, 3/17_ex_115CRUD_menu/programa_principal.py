'''Exercício 115abc - Vamos criar um menu em Python, usando modularização.'''

from menuLib.leiaNum import *
from menuLib.formato import hudMenuOpções
from menuLib.opções import opção

nome_arq = 'cadastros.txt'

try:
    arq = open(nome_arq, 'xt+')
    print(f'\nArquivo \'{nome_arq}\' criado com sucesso!\n')
    arq.close()
except FileExistsError:
    print(f'\nArquivo \'{nome_arq}\' já existe!\n')
finally:
    while True:
        hudMenuOpções()
        op = leiaInt('Sua opção: ')
        opção(op, nome_arq)
