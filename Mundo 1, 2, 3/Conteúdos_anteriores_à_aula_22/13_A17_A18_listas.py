''' Variáveis Compostas

São variáveis que armazenam múltiplos valores ao mesmo tempo. '''

############
## Listas ##
############

#############
## Parte 1 ##
#############

# Formas de declarar uma lista

lista = []
# ou
lista = list()

# Listas são MUTÁVEIS, diferentemente de tuplas. É possível alterar/remover um valor inserido em uma tupla por outro valor.

# Exemplos

lanche = ['hamburguer', 'refrigerante', 'ketchup', 'mostarda'] # Lista normal.

lista = list(range(4,11)) # Lista ordenada.
# No caso acima, a lista irá ter o número 4 na posição 0 e o número 10 (pois o último número é desconsiderado em 'range') na posição 6.

print('0 ',lista)

print('1 ',lanche)

lanche[0] = 'sanduíche' # Troca um elemento por outro.

print('2 ',lanche)

lanche.append('sorvete') # Adiciona um novo elemento à lista em uma nova posição no final.
#IMPORTANTE: Não é possível utilizar 'lanche[nova_posicao] = valor' para adicionar um novo valor no final.

print('3 ',lanche)

lanche.insert(1,'cachorro quente') # Adiciona um novo elemento em uma posição existente, reposicionando o antigo elemento à direita.

print('4 ',lanche)

del lanche[0] # Remove um elemento da lista, reposicionando os outros elementos nas novas posições.
lanche.pop(0) # Sem colocar a posição nos parênteses, essa sintaxe remove o último elemento da lista.
lanche.remove('sorvete') # Remove da lista a primeira ocorrência do termo entre parênteses.

print('5 ',lanche)

if 'sorvete' in lanche: # É possível criar condicionais com elementos de uma lista.
    lanche.remove('sorvete')

lista2 = [1,10,8,9,2,3,7,0,6,5,4]
 
lista2.sort() # Altera a lista, ordenando os elementos dela. Se utilizado dentro de um print retorna 'None'.
print('6 ',lista2)
lista2.sort(reverse=True) # Ordena os elementos na ordem inversa.
print('7 ',lista2)

# Referência
print('\nElementos referenciados')
a = [1, 2, 3, 4]
b = a # Aqui B é igual a A, ou seja, A também será igual a B.
b[0] = 99
print(f'A = {a}\nB = {b}') # Como é possível ver, tantos os elementos da lista A quanto os da B foram alterados.

# Cópia
print('\nElementos copiados')
a = [1, 2, 3, 4]
b = a[:] # Aqui B é igual aos VALORES de A, já A não tem conexão nenhuma com B.
b[0] = 99
print(f'A = {a}\nB = {b}') # Como é possível ver, apenas os elementos da lista B foram alterados.




#############
## Parte 2 ##
#############

# Listas dentro de listas (Listas compostas)
print('\nListas compostas')
dados = ['Maria', 30, 'Roberto', 40]
pessoas = list()

dados.append('José')
dados.append(25)
pessoas += dados[0:2] # NÃO CRIA uma sublista na lista 'pessoas', apenas copia os elementos da lista 'dados' da posição 0 até 1 para a lista 'pessoas'.
pessoas.append(dados[0:2]) # CRIA uma sublista na lista 'pessoas', dentro dessa sublista terá a copia dos elementos da lista 'dados' da posição 0 até 1.
pessoas.append(dados[4:6])
print(f'Lista simples: {dados}')
print(f'Lista composta: {pessoas}')
print(f'Busca em lista composta: {pessoas[2][0][3]}') # Sublista 2 ['José', 25], Elemento 0 ['José'], Posição 3 ['é'] = é

# Referência
print('\nLista referenciada')
a = ['A', 'B', 'C']
b = list()
b.append(a) # Referência
print(f'{'"a" inicial =':<14}', f'{f'{a}':<17}',f'| {b} = "b" inicial (contém referência de "a")')
a[0] = 'D'
a[1] = 'E'
a[2] = 'F'
print(f'{'"a" alterado =':<14}', f'{f'{a}':<17}', f'| {b} = "b" depois da alteração de "a"')
# Os elementos referenciados anteriormente na lista 'b' SÃO alterados, já que os elementos de 'b' estão conectados aos elementos de 'a'.
b[0][0] = 'G'
b[0][1] = 'H'
b[0][2] = 'I' 
print(f'{'"b" alterado =':<14}', f'{f'{b}':<17}', f'| {a} = "a" depois da alteração de "b"')
# Como 'a' está dentro de 'b', ao alterar os valores de 'b', os valores de 'a' também são alterados.

# Cópia
print('\nLista copiada')
a = ['A', 'B', 'C']
b = list()
b.append(a[:]) # Cópia
print(f'{'"a" inicial =':<14}', f'{f'{a}':<17}',f'| {b} = "b" inicial (contem cópia de "a")')
a[0] = 'D'
a[1] = 'E'
a[2] = 'F'
print(f'{'"a" alterado =':<14}', f'{f'{a}':<17}', f'| {b} = "b" depois da alteração de "a"')
# Os elementos copiados anteriormente na lista 'b' NÃO SÃO alterados, já que a copia dos elementos de 'a' para 'b' ocorreu antes das alterações dos elementos de 'a'.
b[0][0] = 'G'
b[0][1] = 'H'
b[0][2] = 'I' 
print(f'{'"b" alterado =':<14}', f'{f'{b}':<17}', f'| {a} = "a" depois da alteração de "b"')
# Como é apenas uma cópia de 'a' dentro de 'b', ao alterar os valores de 'b', os valores de 'a' permanecem inalterados.

# Utilizando 'for' com listas compostas
print('\nEstrutura de repetição com listas compostas!')
cadastro = [['José', 28], ['Maria', 32], ['Roberto', 52]]

for pos in cadastro:
    print(f'{pos[0]} tem {pos[1]} anos de idade.')

# Comando para apagar dados de uma lista
cadastro.clear()
print(cadastro,'\n') # Teste
