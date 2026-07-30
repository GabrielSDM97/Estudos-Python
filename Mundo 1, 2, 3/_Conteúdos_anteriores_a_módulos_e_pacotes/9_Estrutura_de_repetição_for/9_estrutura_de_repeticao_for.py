''' Estrutura de repetição simples

# Para situações que TEM como saber o limite para que uma condição seja alcançada.
# Exemplo: Crie um programa que leia a idade de 10 pessoas...

# Exemplo simples
for contador in range(1,10):
    bloco interno
bloco fim

# Por padrão, o último número do intervalo (range) é desconsiderado, ou seja, acima o loop repetirá de 1 até 9 (9 vezes).

# Estrutura do 'range(início, fim, passo)'
início - Regra de início do loop.
fim - Regra de fim do loop.
passo - Regra de incrementação/redução em cada loop.

# Incremento e redução
Com um intervalo "range(6, 0, -1)" o loop será de 6 até 1, com redução de 1 em 1.
Com um intervalo "range(0, 6, 2)" o loop será de 0 até 5 com incremento de 2 em 2.
E assim por diante... '''

# Exemplo 1
# É possível utilizar apenas um número em parâmetros. No caso abaixo, ocorrerá 5 loops (de 0 a 4).
for c in range(5):
    algo = input('Digite algo: ')
    print(f'{algo}', end='; ')

# Exemplo 2
num1 = int(input('\n\nInício: '))
num2 = int(input('Fim: '))
num3 = int(input('Passos: '))
contador_loop = acumulador_num = 0
# É possível utilizar variáveis nos parâmetros também.
for contador in range(num1, num2, num3):
    print(contador, end='; ')
    contador_loop += 1  # Variável que conta a quantidade de loops.
    acumulador_num += contador # Variável que acumula os valores do range a cada loop.
print(f'\nA quantidade de números é {contador_loop}, e a soma de todos eles é {acumulador_num}.')