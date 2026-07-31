''' Variáveis Compostas
 
São variáveis que armazenam múltiplos valores ao mesmo tempo. '''

############
## Tuplas ##
############

# Forma de declarar uma tupla

tupla = ()

# Tuplas são IMUTÁVEIS. Não tem como alterar/remover um valor inserido em uma tupla por outro valor, ou adicionar um novo valor.

# Exemplo

lanche = ('hamburguer', 'refrigerante', 'ketchup', 'mostarda') # 0, 1, 2, 3 ou -4 -3 -2 -1

print(lanche[-4:4]) 

# lanche[1] = 'coca-cola' - Após a criação da tupla 'lanche' acima, essa sintaxe resultaria em um erro justamente por serem imutáveis.

# Utilizando uma tupla como range para um 'for'.
print('\nPrimeira variação')
for comida in lanche: # 'comida' herda as strings de lanche.
    print(f'eu vou comer {comida} na posição')

print('\nSegunda variação')
for pos, comida in enumerate(lanche): # 'pos' (ou qualquer outro nome no lugar) herda as posições em int de 'lanche', 'comida' herda as strings de 'lanche'.
    print(f'eu vou comer {comida} na posição {pos}') # 'pos' é utilizada para indexar posições quando utilizada com 'enumerate()'

print('\nTerceira variação')
for comida in range(0,len(lanche)): # 'comida' herda os valores int de range.
    print(f'eu vou comer {lanche[comida]} na posição {comida}') # A posição sera os números int do range 'comida'

# Exemplo com números
A = (1,2,3,4)
B = (4,3,2,1)
C = B+A # Ele cria um nova tupla com todos os números das tuplas inseridas e na ordem que foram inseridas.

print('\n',C)
# Index funciona semelhantemente à 'string.find('X')', só que para números.
print(f'\nValor da posição 3 da tupla C: {C.index(3)}') 
print(f'\nPosição do 1º valor 2 na tupla a partir da pos 3: {C.index(2, 3)}\n')

# Em Python é possível colocar tanto string quanto números em uma só tupla, diferentemente de outras linguagens de programação.
pessoa = ('José', 39, 'Casado', 1.75, 'Marceneiro')
print(pessoa)

# Para remover uma túpla usa-se 'del(túpla)'
# del(pessoa[0]) - Retornaria erro já que não é possível nem remover nem modificar apenas um item de um túpla, pois é imutável.
del(pessoa)
# print(pessoa) - Retornaria um erro já que a tupla 'pessoa' foi removida.

print(f'{sorted(lanche)}') # Não altera a tupla. Por padrão, organiza em ordem alfabética.
print(f'{sorted(lanche, reverse=True)}') # Organiza na ordem inversa. (parâmetro 'reverse=True' serve para isso.)

print()

# Comando para somar todos os dados númericos de uma lista/tupla/dicionário
add = (1,2,3,4,5)
print(sum(add))

# Operadores de alinhamento
a = (1,2,3)
b = 1

print(f'{str(a):20}') # Para alinhar uma lista/tupla/dicionário, deve-se transformar a variável em uma string utilizando 'str()'.
print(f'{(b):20}') # Já para valores numéricos ou string, não é necessário utilizar 'str()'.

# Utilizando o método `separador.join(iterável)` para juntar índices de uma tupla em uma nova variável.
# O separador de join deve ser sempre uma string.
nomeCompleto = ("Roberto", "Silva")
string = " ".join(nomeCompleto)
print(string)

# Utilizando uma variável de string como separador de join.
número = ("Olá", "Mundo!")
separador = ", "
string = separador.join(número)
print(string)

# O método join pode ser utilizado da mesma forma com listas. 
# Já com dicionários existe uma pequena diferença que será tratada na aula sobre dicionários.
