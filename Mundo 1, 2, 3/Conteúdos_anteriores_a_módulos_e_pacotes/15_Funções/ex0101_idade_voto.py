''' Exercício 101 - Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições. '''


def voto(ano):
    from datetime import date
    limpar = '\033[m'
    vermelho = '\033[91m'
    verde = '\033[92m'
    amarelo = '\033[93m'
    global idade
    idade = date.today().year - ano
    if idade < 16:
        return f'{vermelho}proibido{limpar}'
    elif 16 <= idade < 18 or idade > 70:
        return f'{amarelo}opcional{limpar}'
    else:
        return f'{verde}obrigatório{limpar}'


print(f'Seu voto é {voto(1997)}, pois você tem {idade} anos!')
