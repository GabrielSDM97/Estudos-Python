''' Quebra de repetição while 

# Estruturas para quebrar 'while' durante um loop.

# Exemplo
while True:
    if condicao:
        bloco
    if condicao:
        bloco
        break <-- Quebra o loop e vai para o bloco final.
bloco final '''

num = 0

# Exemplo de loop infinito
while True:
    if num == 100:
        break  # Finaliza o 'while' antes do loop finalizar.
    num += 1
    print(f'{num}.' if num == 100 else f'{num}, ', end='')
print('\nFIM!!!')

print()

# Existe também a cláusula 'else' em while. Ela é executada quando a condição de while se torna False.
a = 9
b = 8

while a <= b:
    print(f"{a};", end=' ')
    if a == b:
        break # Pula o tanto o 'while' quanto o 'else'.
    a += 1
else:
    print(f"O valor {a} é maior que {b}. Insira um valor menor!")
print('FIM!')
