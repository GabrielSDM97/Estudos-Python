''' Estrutura de repetição while 

# Para situações que NÃO TEM como saber o limite para que uma condição seja alcançada.
# Exemplo: Crie um programa que leia a idade de TODAS as pessoas que quiserem participar do evento...

# Exemplo
while condição(flag):
    bloco interno
bloco final '''

''' Uma 'flag' e é uma variável booleana usada para controlar quando o loop deve continuar ou parar. 
Enquanto a flag for True, o loop continua; quando ela vira False, o loop para. '''

# Exemplo
num = int(input('Número inícial: '))
resposta = 'S'
contador_loop = acumulador_num = 0

while resposta in 'Ss': # Enquanto o usuário digitar "S" quando requisitado, o loop ocorrerá denovo, e de novo...
    print(num, end='; ')
    contador_loop += 1 # Variável que conta a quantidade de loops.
    acumulador_num += num # Variável que acumula os valores de 'num' a cada loop.
    num += 1
    resposta = str(input('\nDeseja continuar? [S/N] ').strip()[0])
print(f'\nA quantidade de números é {contador_loop}, e a soma de todos eles é {acumulador_num}.')

