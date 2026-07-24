# A função sorted() permite ordenar iteráveis usando uma função de chave personalizada.
# Sintaxe: sorted(iterável, key=função, reverse=False)
# Exemplo: sorted([3, 1, 2], key=lambda x: -x) # Ordena de forma decrescente.

lista = ["bask3t", "ment0", "vent1"]

# Função de chave (key function): recebe um item do iterável e retorna o valor usado na comparação.
def ordem_numérica(palavra):
    for caractere in palavra:
        if caractere.isnumeric():
            return int(caractere)
    return 0

# O sorted() aplica a função a cada item, ordenando a lista com base nos inteiros retornados.
print(sorted(lista, key=ordem_numérica))