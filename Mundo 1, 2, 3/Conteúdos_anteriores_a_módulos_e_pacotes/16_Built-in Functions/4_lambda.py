# Uma função lambda é uma pequena função anônima sem nome.
# 
# Uma função lambda pode ter qualquer quantidade de parâmetros, porém só pode ter uma expressão (retorno).
# É muito utilizada com funções de  que disponibilizam argumentos, como map(), sorted() e filter()
#
# Sintaxe: lambda parâmetros : expressão
# Exemplo com map:    map(lambda parâmetro1, parâmetro2: expressão, argumento1, argumento2)
# Exemplo com filter: filter(lambda parâmetro: expressão, argumento)
# Exemplo com sorted: sorted(argumento, key = lambda parâmetro: expressão)


# Refazendo o exemplo da aula "2_map.py"
frutas1 = ("Maçã", "Uva", "Laranja")
frutas2 = ("Goiaba", "Banana", "Pera")

print(list(map(lambda f1, f2: f1+f2, frutas1, frutas2)))


# Refazendo o exemplo da aula "3_filter.py"
lista = ["maçã", "banana", "abacate", "cereja", "pera"]

print(list(filter(lambda fruta: 'e' in fruta, lista)))


# Refazendo o exemplo da aula "4_sorted.py"
lista = ["bask3t", "ment0", "vent1"]

print(list(sorted(lista, key=lambda palavra: [num for num in palavra if num.isdigit()])))


# Utilizando lambda dentro de outra função
def myfunc(n):
  # Retorna a função lambda
  return lambda a : a * n

# Envia o argumento 3 para o parâmetro "n" de "myfunc"
mytripler = myfunc(3)

# Utiliza a função lambda retornada para "mytripler" e 
# insere em seu parâmetro o valor a ser multiplicado por "n"
print(mytripler(11))
