''' Variáveis Compostas
 
São variáveis que armazenam múltiplos valores ao mesmo tempo. '''

#################
## Dicionários ##
#################

# Formas de declarar um dicionário

dados = dict()
# ou
dados = {}

# Exemplo
dados = {'nome': 'Gabriel', 'idade': 28}

print(f'\n1. {dados['nome']}')

# Altera um valor de uma chave.
dados['nome'] = 'Roberto'

# Adiciona uma nova chave e seu valor.
dados['sexo'] = 'M'

# Remove uma chave juntamente com seu valor.
del dados['idade']

# Retorna todos os valores de um dicionário ('Gabriel' e 'M' no caso da variável 'dados')
print(f'\n2. {dados.values()}')

# Retorna todos as chaves de um dicionário ('nome' e 'sexo' no caso da variável 'dados)
print(f'\n3. {dados.keys()}')

# Retorna chaves e valores de um dicionário
print(f'\n4. {dados.items()}')

# Utilizando a estrutura de repetição 'for' com dicionários.
# Opção semelhante a enumerate (de tuplas e listas), só que para dicionarios.
for key, value in dados.items():
    print(f'{key}:{value}')

# Utilizando dicionários dentro de uma lista
cadastro = [{'nome': 'Gabriel', 'idade': 28}, {'nome': 'José', 'idade': 32}, {'nome': 'Roberto', 'idade': 45}]

# Dentro de aspas simples, deve-se usar aspas duplas.
print(f'\n5. {cadastro[0]["nome"]}\n')

# Copiando dados de dicionários para uma lista
nome_completo = dict()
cadastro = list()
nome = list()

for c in range(0, 3):
    nome_completo['nome'] = str(input('Digite um nome: '))
    nome_completo['sobrenome'] = str(input('Digite um sobrenome: '))
    # Utiliza-se '.copy()' em vez da técnica de fatiamento '[:]' para copiar um dicionário inteiro para uma lista.
    cadastro.append(nome_completo.copy())
    # A tecnica de fatiamento ainda pode ser utilizada em dicionários, porém apenas para copiar um valor específico de uma chave, só que em vez de usar [:] utiliza-se [chave].
    nome.append(nome_completo['nome'])
print(f'6. {cadastro} --- {nome}')
# Sem utilizar o '.copy()' o último valor inserido se repetirá 3 vezes dentro da lista, já que se torna uma referência e não uma cópia.



## Organizando um dicionário ##

dicionário = {'A': 1, 'B': 5, 'C': 2, 'D': 4, 'E': 3}

''' A função 'sorted()', além de sortear, transforma um dicionário e suas chaves em uma lista com tuplas.
Para organizar essas tuplas, utiliza-se a função anônima 'lambda x: x[pos]' no parâmetro 'key='(regras de organização) dentro da função 'sorted()'.
Abaixo configurei para que a organização ocorresse baseada no tipo de valor da posição 1 das tuplas da lista 'dicionário', ou seja, baseada em ordem numérica. '''
organizado = sorted(dicionário.items(), key=lambda posição: posição[1], reverse=True)

print(f'\n7. {organizado}') # Resultado

''' É possível também organizar utilizando a função 'itemgetter()' da biblioteca 'operator'.
Esta função consegue acessar qualquer valor ou elemento de tuplas, listas e até dicionários apenas com um número referente à posição deste dentro da lista.

# Exemplo

from operator import itemgetter

organizado = sorted(dicionário.items(), key=itemgetter(1), reverse=True)'''  # Pegando o item na posição 1 do dicionário.'''

# Um dicionário dentro de uma função 'sorted()' passa a ser uma lista, as chaves passam a ser tuplas e os valores, elementos das tuplas.
