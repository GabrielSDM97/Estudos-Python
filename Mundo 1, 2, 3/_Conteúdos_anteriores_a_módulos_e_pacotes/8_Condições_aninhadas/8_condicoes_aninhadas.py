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


# Em operador ternário não temos "elif". Segue um exemplo de operador ternário aninhado abaixo e a explicação.
# Exemplo:
num = 3
x = "Um" if num == 1 else "Dois" if num == 2 else "Três" if num == 3 else "Quatro" if num == 4 else "Outro número..."
# Explicação:
# "Um" if num == 1 - Atribui "Um" a "x" se num for igual a 1
# else "Dois" if num == 2 - Atribui "Dois" a "x" se num for igual a 2
# else "Três" if num == 3 - Atribui "Três" a "x" se num for igual a 3
# else "Quatro" if num == 4 - Atribui "Quatro" a "x" se num for igual a 4
# else "Outro número" - Atribui "Outro número" a "x" se nenhuma das condições anteriores forem atendidas
print(x)

print(20*'-=','FIM',20*'=-')
