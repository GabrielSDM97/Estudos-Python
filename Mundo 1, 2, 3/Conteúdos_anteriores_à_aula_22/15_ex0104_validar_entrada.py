''' Exercício 104 - Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 
a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.

Ex: n = leiaInt('Digite um n: ') '''


def leiaInt(msg):
    while True:
       valor = str(input(f'{msg}\033[92m'))
       print('\033[m')
       if valor.replace('-','').isnumeric():
            return f'\033[96m{valor}\033[m'
       else:
            print(f'\033[91mValor inválido, tente novamente!\033[m')


# Programa principal
n = leiaInt('\nDigite um valor: ')
print(f'Você digitou o número {n}!')
