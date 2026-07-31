
# A função "map()" executa a função especificada para cada ítem individualmente em um objeto iterável (lista, tupla, etc...).
# O ítem é enviado para a função como parâmetro.

# Sintaxe: map(função, iterável)
# Exemplo: x = map(numeros, [1,2], [2,4], [4,8])

def juntarFrutas(fruta1, fruta2):
    return f1 + f2

frutas1 = ("Maçã", "Uva", "Laranja")
frutas2 = ("Goiaba", "Banana", "Pera")

# Concatenação direta: une as duas tuplas inteiras, resultando em uma única tupla de 6 itens.
a = juntarFrutas(frutas1, frutas2)

# Mapeamento: aplica aos parâmetros da função elemento a elemento (índice 0 com 0, 1 com 1, etc.).
b = map(juntarFrutas, frutas1, frutas2)

# Note a diferença na estrutura de dados resultante.
print(a)

# map() retorna o endereço do objeto iterado, sendo necessário utilizar list() para materializar os dados em uma lista.
print(list(b))