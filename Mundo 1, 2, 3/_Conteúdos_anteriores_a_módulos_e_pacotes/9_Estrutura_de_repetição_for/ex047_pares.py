''' Exercício 47 - Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50. '''

# Melhor pular de 2 em 2 do que colocar "if contador % 2 == 0" por questões de otimização, já que ocorrerá menos iterações.
# Quanto menos iterações = Melhor performance do programa.

for contador in range(2,51,2):
    print(contador,end=', ')
print('FIM!!!')
