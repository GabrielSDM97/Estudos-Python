''' Exercício 114 - Crie um código em Python que teste se o site pudim está acessível pelo computador usado. '''

import requests

try:
    site = requests.head('https://pudim.com.br')
except requests.exceptions.RequestException:
    print(f'O site Pudim está offline')
else:
    print(f'O site Pudim está online')
