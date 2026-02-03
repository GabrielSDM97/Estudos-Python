''' Condições aninhadas

if objeto.metodo():
    Bloco 1
elif objeto.metodo():
    Bloco 2
elif objeto.metodo():
    Bloco 3
else:
    Bloco 4
Bloco final

A condição 'elif' pode ser repetida infinita vezes. Já 'else' deve ser usado apenas no final ou não ser usado.

'''

# Exemplo

nome = str(input('Digite 2 palavras:')).strip().split()

if len(nome) > 2 or len(nome) < 2:
    print('Você inseriu uma quantia diferente de 2 palavras, tente novamente!')
elif len(nome[0]) > len(nome[1]):
    print(f'A palavra "{nome[0]}" é a maior')
elif len(nome[1]) > len(nome[0]):
    print(f'A palavra "{nome[1]}" é a maior')
else:
    print('As duas palavras tem o mesmo tamanho.')
print(20*'-=','FIM',20*'=-')
