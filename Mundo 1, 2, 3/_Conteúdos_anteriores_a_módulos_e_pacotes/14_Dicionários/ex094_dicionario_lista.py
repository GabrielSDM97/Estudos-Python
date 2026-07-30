''' Exercício 94 - Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média '''

cadastros = list()
pessoa = dict()

while True:
    while True:
        pessoa['nome'] = str(input('Nome: '))
        if pessoa['nome'].replace(' ', '').isalpha() == False:
            print('Nomes só podem ter caracteres alfabéticos. Tente novamente!')
        else:
            break
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ').strip()[0])
        if pessoa['sexo'] not in 'MmFf':
            print('Valor inválido, tente novamente!')
        else:
            break
    pessoa['idade'] = int(input('Idade: '))
    cadastros.append(pessoa.copy())
    continuar = ''
    while True:
        continuar = str(input('\nDeseja cadastrar mais uma pessoa? [S/N] '))
        if continuar not in 'SsNn':
            print('Resposta inválida, tente novamente!')
        else:
            break
    if continuar in 'Nn':
        break
print(20*'~~~')
print(f'A) Quantas pessoas foram cadastradas: {len(cadastros)}')

sum_idade = 0
for pos, dicionário in enumerate(cadastros):
    sum_idade += dicionário['idade']
media_idade = sum_idade/len(cadastros)
print(f'B) Média de idade: {media_idade:.0f} anos')

print(f'C) As mulheres cadastradas foram:', end=' ')
for pos, dicionário in enumerate(cadastros):
    if dicionário['sexo'] == 'F':
        print(dicionário['nome'],end='; ')

print(f'\nD) Pessoas com idade acima da média: ')
for pos, dicionário in enumerate(cadastros):
    if dicionário['idade'] > media_idade:
        print(f'| nome = {dicionário['nome']:<14}| sexo = {dicionário['sexo']:<2}| idade = {dicionário['idade']:<4}|')
print('~~~ FIM! ~~~')
