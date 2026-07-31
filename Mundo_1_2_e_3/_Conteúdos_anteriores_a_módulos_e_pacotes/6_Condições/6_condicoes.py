# Padrão de sintaxe: 'objeto.metodo()'

''' 

-- Condição simples --

if objeto.metodo():
    bloco True
bloco final

-- Condição composta --

if objeto.metodo():
    bloco True
else:
    bloco False
bloco final

'''

# Obs.: Em Python, a identação dos blocos é obrigatória nas condições.

# Exemplo

num = int(input('Insira um número: '))

print('\nCondição padrão (Recomendado) / Estruturado')
if num%2 == 0:
    print(f'\nO número {num} é par.')
else:
    print(f'O número {num} é impar.')
print(20*'-','FIM!',20*'-','\n')


print('Condição simplificada / Operador ternário')
print(f'\nO número {num} é par.' if num%2 == 0 else f'O número {num} é impar.')
# Em .format(): print('\nO número {} é par.'.format(num) if num%2 == 0 else 'O número {} é impar.'.format(num))

# É possível utilizar operador ternário para escolher resultados diferentes para uma variável
# Exemplo:
x = f"{num} é maior que 5!" if num > 5 else f"{num} é menor ou igual a 5!"
print(x)

print(20*'-','FIM!',20*'-')


# Estrutura "match case" <- Equivalente a "switch case", só que para Python.
value = 2

# Diferentemende de "switch case", "match case" não precisa de "break" em cada "case" para parar a execução da estrutura.
match value:
    case 1:
        result = "um"
    case 2:
        result = "dois"
    case 3:
        result = "três"
    case _: # Equivalente a "default" em "switch case"
        result = "desconhecido"

print(result)
