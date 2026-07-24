# A função filter() retorna o iterador com os ítens aprovados pela função que testou
# ítem por ítem do iterável.

# Sintaxe: filter(função, iterável)
# Exemplo: x = filter(pares, [1,2,3,4,5])


def contem_e(fruta):
    
    # Retorna booleano. Se for verdadeiro, a string é adicionada em um índice do objeto iterador.
    return 'e' in fruta

lista = ["maçã", "banana", "abacate", "cereja", "pera"]

# filter() avalia um elemento por vez. Retorna um iterador com os itens aprovados.
resultado = filter(contem_e, lista)

# Materializando os dados do iterador em uma lista.
print(list(resultado))
