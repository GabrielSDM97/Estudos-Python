# Variáveis de cores
limpar = '\033[m'
verde = '\033[92m'
amarelo = '\033[93m'
ciano = '\033[96m'

''' Exercício 69 - Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.  '''

maior_idade = homem = mulher_jovem = 0

while True:
    print(limpar)
    print(20*f'=',f'\n{'Cadastro de pessoa':^20}')
    print(20*'=')
    idade = int(input(f'\n{limpar}Idade da pessoa:{verde} '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input(f'{limpar}Sexo da pessoa [M/F]:{verde} ').strip()[0])
        if sexo not in 'MmFf':
            print(f'\n{limpar}Dado inválido, tente novamente!')
    if idade > 18:
        maior_idade += 1
    if sexo in 'Mm':
        homem += 1
    if sexo in 'Ff' and idade < 20:
        mulher_jovem += 1
    print(f'\n{amarelo}Cadastro efetuado com sucesso!{limpar}')
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input(f'\n{limpar}Deseja fazer um novo cadastro? [S/N]{verde} ').strip()[0])
        if continuar not in 'SsNn':
            print(f'{limpar}Resposta inválida, tente novamente!')
    if continuar in 'Nn':
        break
print(limpar)
print(10*'~','Análise geral de dados cadastrados',10*'~')
print(f"""{limpar}A) Pessoas com mais de 18 anos: {ciano}{maior_idade}{limpar}
B) Homens cadastrados: {ciano}{homem}{limpar}
C) Mulheres com menos de 20 anos: {ciano}{mulher_jovem}{limpar}\n""")
