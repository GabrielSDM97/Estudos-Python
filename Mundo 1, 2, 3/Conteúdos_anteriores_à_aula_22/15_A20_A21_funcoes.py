''' Funções

Função é um bloco de código reutilizável.

Existem funções 'built-in' como 'print()', por exemplo, e existem funções feitas por usuário, que serão o assunto desse arquivo.

## Não confundir funções com metodos, objetos e classe. ##

| print("oi") | ✅ | Função | embutida Pré-definida no Python para exibir mensagens.
| minha_funcao() | ✅ | Função | definida por você Criada com def minha_funcao():
| lista.append(1) | ❌ | Objeto.Método |  append pertence ao objeto lista (é uma função dentro de um objeto).
| int("10") | ❌ | Construtor de classe | int é uma classe, e int("10") cria uma instância dela (número inteiro).

Funções de usuário são utilizadas para facilitar rotinas.

Rotinas são certas funções que usamos repetidamente durante a criação de programas.

Para criar uma rotina em uma função de usuário utiliza-se 'def nomedafunção():'

'''

#############
## Parte 1 ##
#############

# Exemplo (FUNÇÃO)
def linha():
    print(15*'-')
# É obrigatório ter 2 ou mais linhas entre DEFINIÇÃO DE FUNÇÂO (def) e o PROGRAMA PRINCIPAL.

# PROGRAMA PRINCIPAL
linha()
print('Curso de python')
linha()


### Parâmetros ###
# 'mensagem' é um PARÂMETRO (espaço reservado para um valor que será recebido)
def título(mensagem):
    # Lugar reservado para argumentos que serão utilizado quando essa função for CHAMADA.
    print(len(mensagem)*'~')
    print(f'\033[1;92m{mensagem}\033[m')
    print(len(mensagem)*'~')

# CHAMADA DA FUNÇÃO
# 'Teste' é o ARGUMENTO (valor real enviado para o parâmetro 'mensagem')
título('Curso de python')


# Utilizando para cálculos
def soma(a, b):
    s = a + b
    print(f'A soma de {a} e {b} é {s}\n')


# Programa principal
soma(2, 3)
# Também é possível explicitar o valor de cada parâmetro dessa maneira.
soma(a=10, b=20)


## Desempacotar parâmetros ##
# Com a técnica de desempacotamento, é possível utilizar múltiplos valores em um só parâmetro em Python utilizando o operador '*' juntamente com o parâmetro.
def contador(*nums):
    print(nums, end=' ') # Por padrão, vários números desempacotados em um parâmetro ficam em uma tupla.
    print(f'Soma = {sum(nums)}')

# Programa principal
contador(1, 2, 0, 4, 1)


## Manipulando listas ##
def duplicar(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(f'Duplicada: {lst}')

# Programa principal
lista = [1, 2, 0, 4, 1]
print(lista, end=' ')
duplicar(lista)


## Parâmetro 'flush = True' ##
# É utilizado na função 'print()'
# Flush serve para atualizações em tempo real, principalmente em laços de repetição temporizados.
# Exemplo:
from time import sleep

def numeros(num):
    num += 1
    print('\nSem "flush = True"')
    for c in range(num):
        # Sem flush, valores em linha gerados em um laço de repetição só aparecem quando ocorrer a inserção de uma nova linha.
        print(f'{c}', end=' ')
        sleep(0.25)
    print('\nCom "flush = True"')
    for c in range(num):
        # Já com flush, qualquer mudança em linha é mostrada na tela.
        print(f'{c}', end=' ', flush=True)
        sleep(0.25)


numeros(5)
print('\n')



#############
## Parte 2 ##
#############

### Interactive help ###
# 'help(função)' - Função que mostra tudo o que é possível fazer com determinada função.
# Ex:

help(input) # Forma 1 (Mais prática e recomendada)
print(input.__doc__) # Forma 2
print()

# Para ver informações de uma biblioteca, importá-la primeiro.
'''
import random
help(random)
'''

### Docstrings ###
# Servem par adicionar instruções para uma função criada pelo usuário.
# Para criar uma docstring, devem ser inseridas 3 aspas duplas na primeira linha abaixo da 'def'.
# Ex:
def vermelho(msg):
    """
    Utilize desta forma: 'vermelho('Texto aqui')'. Assim, todo conteúdo dentro desta função ficará com a cor vermelha.
    """
    print('\033[91m')
    print(msg)
    print('\033[m')


help(vermelho)


### Parâmetros opcionais ###
def somar(a=0, b=0, c=0): # Valor padrão 'a','b' e 'c' serão 0 caso não recebam nenhum valor.
    soma = a + b + c
    print(soma)

# Programa principal
somar(1,2)
somar(c=7)
somar()


### Escopos de variáveis e importação (local e global) e formas de utilizá-las ###

## Variável de escopo global ##
def calculo():
    print(n) # (ler primeiro o comentário abaixo)..., e como podemos ver, após o chamado desta função, a variável global 'n' pode ser reutilizada aqui também.


n = 2 # Exemplo de VARIÁVEL GLOBAL. Ela pode ser reutilizada em qualquer lugar depois da declaração dela... (continuar leitura na função acima)
calculo() # Chamado da função 'calculo()' após a declaração da variável 'n'.


## Variável de escopo local ##
def calculo(n1, n2):
    x = n1 + n2 # Já uma variável dentro de uma função é considerada uma VARIÁVEL LOCAL...


calculo(1,2)
# print(x) ...não podendo ser reutilizada fora da função onde foi criada (Executando o 'print(x)' accaretaria em erro).
print()


## Variável global e local com mesmo nome ##
def teste1(b):
    a = 2 # Variável 'a' LOCAL.
    print(f'Dentro "a" vale {a}') # 'a' terá o valor da variável local 'a'
    print(f'Dentro "b" vale {b}') # 'b' terá o valor da variável global 'a'


a = 10 # Variável 'a' GLOBAL.
teste1(a)
print(f'Fora "a" vale {a}') # Valor da variável 'a' global.
print()


## Alterando valor de variável global dentro de uma função ##
# Utiliza-se a declaração de escopo 'global nomedavariável' antes de declarar um novo valor para uma variável global dentro da função.
# Exemplo:
def teste2(b):
    global a # Definindo escopo como global para a variável 'a', como já existe uma variável 'a' global, as duas se tornam uma.
    a = 2 # Alterando valor da variável 'a' global.
    print(f'Dentro "a" vale {a}') # 'a' terá o novo valor da variável global 'a'
    print(f'Dentro "b" vale {b}') # 'b' terá o antigo valor da variável global 'a', já que a declaração do novo valor ocorreu depois de 'b' receber o antigo valor dela.

a = 10 # Variável 'a' global.
teste2(a)
print(f'Fora "a" vale {a}') # O novo valor global de 'a' declarado na função acima contará fora da função também.
print()

## Criando um variável global a partir de uma função ##
def teste3():
    global a
    a = 10

teste3()
print(f'{a}\n')


## Retornando valores ##
# A instrução 'return' encerra a execução da função e devolve um valor para quem chamou a função para que este valor possa ser utilizado fora da função. 
# Se não usar 'return', a função retorna 'None' por padrão.
print('Sem "return"')
def soma(a=0, b=0):
    sum = a + b
# Não retorna nada, ou seja, 'None'

r1 = soma(1,2)
r2 = soma(2,3)
r3 = soma(3,4)
print(f'As somas deram {r1}, {r2} e {r3}')
print()

print('Com "return"')
def soma(a=0, b=0):
    sum = a + b
    return sum # Retona o valor da soma de a + b.

r1 = soma(1,2)
r2 = soma(2,3)
r3 = soma(3,4)
print(f'As somas deram {r1}, {r2} e {r3}')
print()

# É possível retornar também valores booleanos, inteiros, float, string, listas, dicionários, tuplas, etc...
# Exemplo
def ParÍmpar(num=0):
    if num % 2 == 0:
        return True
    else:
        return False

número = 8
print(f'O número {número} é', end=' ')
if ParÍmpar(número): # A condição 'if', por natureza, retorna valores verdadeiros ou seja, ou seja, requer 'True' de return.
    print('Par!')
else: # Já o 'else', por natureza, retorna valores falsos, ou seja, requer 'False' de return.
    print('Ímpar!')
print()
# IMPORTANTE! O 'return', além de retornar valores, ele também encerra a função ali mesmo, assim como o 'break' faz em laços de repetição (while e for).

## Importação local e global ##
def ListaAleatoria(num=1):
    from random import randint # É possível importar dentro de uma função, otimizando o programa, já que as funções da importação terão escopo local.
    c = 1
    while c <= num:
        lista.append(randint(1,100))
        c += 1
    return lista

lista = list()
print(ListaAleatoria(10))
