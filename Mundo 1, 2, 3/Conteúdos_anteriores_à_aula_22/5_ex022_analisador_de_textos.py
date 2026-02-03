''' Exercício 22 - Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome. '''

nome = str(input('Digite o seu nome: ').strip())

print(f'Seu nome em maiúsculas é: \033[92m{nome.upper()}\033[m')
print(f'Seu nome em minúsculas é: \033[92m{nome.lower()}\033[m')
# Outra forma de fazer o metodo format abaixo é: ".format(len(''.join(nome.split())))"
print(f'A quantidade de letras no seu nome é: \033[92m{len(nome) - nome.count(' ')}\033[m')
print(f'A quantidade de letras no seu primeiro nome é: \033[92m{len(nome.split()[0])}\033[m')
