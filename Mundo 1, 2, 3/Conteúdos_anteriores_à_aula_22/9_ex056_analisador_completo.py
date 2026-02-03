# Variáveis de cores
limpar = '\033[m'
negrito = '\033[1m'
verde = '\033[92m'
ciano = '\033[93m'

''' Exercício 56 - Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos. '''

idade_homem_velho = qtd_mulher_jovem = soma_idade = 0

for pessoas in range (1,5):
    print(7*'-=',f'{pessoas}ª pessoa',7*'=-')
    nome = str(input(f'Nome:{verde} ').strip().capitalize())
    idade = int(input(f'{limpar}Idade:{verde} '))
    sexo = str(input(f'{limpar}Sexo:{verde} ').strip())
    print(limpar)

    if sexo in 'Mm' and idade > idade_homem_velho: # Homem mais velho
        nome_homem_velho = nome
        idade_homem_velho = idade
    elif sexo in 'Ff' and idade < 20: # Quantidade de mulheres com menos de 20 anos
        qtd_mulher_jovem += 1

    soma_idade += idade 
    media_idade = soma_idade/4 # Média idade

print(f"""Média de idade do grupo: {negrito}{ciano}{media_idade:.0f}{limpar}.
      \nNome e idade do homem mais velho do grupo: {negrito}{ciano}{nome_homem_velho}; {idade_homem_velho} anos{limpar}.
      \nQuantidade de mulheres com menos de 20 anos: {negrito}{ciano}{qtd_mulher_jovem}{limpar}""")
