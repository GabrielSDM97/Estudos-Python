''' Exercício 2 - Crie um progama que leia o nome de uma pessoa e mostre uma mensagem de boas vindas na tela. '''

nome = input('Digite seu nome: ')

print(f'\nBem-vindo, \033[32m{nome}\033[m!')
# A sintaxe acima é a forma moderna equivalente a "print('Bem-vindo,', nome + '!')".