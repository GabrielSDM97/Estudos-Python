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
print(20*'-','FIM!',20*'-')
