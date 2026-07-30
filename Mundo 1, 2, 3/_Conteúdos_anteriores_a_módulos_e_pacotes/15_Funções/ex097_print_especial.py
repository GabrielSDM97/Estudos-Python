''' Exercício 97 - Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável. 
Ex:
escreva('Olá, Mundo!')
Saída:
~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~

'''

def escreva(texto):
    print(f'\n{len(texto)*'~'}')
    print(f'{texto}')
    print(len(texto)*'~')


# Programa principal
escreva(str(input('Digite algo: ')))
