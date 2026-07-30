''' Módulos

Módulos são pacotes/bibliotecas externos que podem ser importados utilizando o comando "import"

(importar todos os nomes)
import nomes

(importar apenas gabriel de nomes)
from nomes import gabriel

Tais sintaxes devem ser colocadas no início de um arquivo python.

IMPORTANTE!!! É recomendado pesquisar por fora cada função das bibliotecas/pacotes.

'''
# Exemplo importando todas as funções de uma biblioteca.
import math

# Quando uma biblioteca é importada por completo, se torna obrigatório colocar o nome dela juntamente a toda função, exemplo: "math.sqrt()".
num = float(input('Insira um número: '))
raizq = math.sqrt(num)

print(f'\nRaiz de {num} é {math.ceil(raizq):.2f}')

print(20*'--')

# Exemplo importando funções específicas de uma biblioteca.
from math import sqrt, floor

# Já quando importamos funções específica de um biblioteca, não precisamos citar o nome dela, exemplo: "sqrt()".
raizq2 = sqrt(num)

print(f'\nRaiz de {num} é {floor(raizq2):.2f}')

print(20*'--')