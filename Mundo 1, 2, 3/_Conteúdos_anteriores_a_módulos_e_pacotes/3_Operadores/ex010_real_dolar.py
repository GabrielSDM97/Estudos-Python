''' Exercício 10 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. '''

print(10*f'\033[93m-=', 'Reais para Dólares', 10*f'=-', f'\033[m\n')

real = float(input('Digite um valor em real:\033[92m R$'))

print('\033[m')
print(f'Com R${real} é possível comprar ${(real / 5.50):.2f}.')