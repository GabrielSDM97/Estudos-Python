from datetime import date

# Variáveis de cores
limpar = '\033[m'
verde = '\033[92m'

''' Exercício 39 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo. 

Desafio extra: verifique o sexo de quem está inserindo os dados, se for feminino, não é nececessário o alistamento. '''

ano_nascimento = int(input(f'Digite o seu ano de nascimento:{verde} '))
sexo = int(input(f'{limpar}Digite 1 para masculino e 2 para feminino:{verde} '))
print(limpar)
idade = date.today().year - ano_nascimento

if sexo == 1:
    print(f'Você nasceu em {ano_nascimento}. Atualmente em {date.today().year} você tem {idade} anos.\n')
    if idade == 18:
        print('Aliste-se IMEDIATAMENTE!!!')
    elif idade < 18:
        idade_alistamento = 18 - idade
        ano_alistamento = date.today().year + idade_alistamento
        print(f'Você ainda não está em tempo de se alistar. Seu ano de alistamento será em {ano_alistamento}. Aguarde {idade_alistamento} ano/anos.')
    else:
        idade_alistamento = idade - 18
        ano_alistamento = date.today().year - idade_alistamento
        print(f'Você não tem mais idade de se alistar. Você deveria ter se alistado há {idade_alistamento} ano/anos. Seu ano de alistamento foi em {ano_alistamento}.')
elif sexo == 2:
    print('Você não precisa se alistar!')
else:
    print('Código inválido referente ao sexo, tente novamente!')
