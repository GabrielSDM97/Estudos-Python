# Compreensão de listas, ou inline for, oferecem uma sintaxe curta quando você quer criar uma nova lista baseada
# em valores de uma lista/tupla/dicionário existente.

# Sintaxe: [expressão for item in iterável if condição]
# Exemplo: x = [n*2 for n in range(10) if n % 2 == 0]

# Exemplo: Baseado em uma lista de frutas, você quer uma nova lista, contendo apenas as
# frutas contendo a letra "e".

frutas = ["Maçã", "Uva", "Laranja", "Goiaba", "Banana", "Pera"]
resultado1 = list()

# Sem compreensão de list você terá que escrever um bloco for tradicional com uma condição de teste dentro:
for fruta in frutas:
    if 'e' in fruta:
        resultado1.append(fruta)
print("1", resultado1)

# Com compreensão de lista você pode fazer tudo isso em uma só linha de código:
resultado2 = [fruta for fruta in frutas if 'e' in fruta]
print("2", resultado2)

# É possível também utilizá-lo diretamente em uma print
print("3", [fruta for fruta in frutas if 'e' in fruta])
