''' Operadores aritméticos

A + B : Adição
A - B : Subtração
A * B : Multiplicação
A ** B ou pow(A,B) : Potênciação
A / B : Divisão real (quociente real completo)
A // B : Divisão inteira (parte inteira do quociente)
A % B : Resto de divisão (apenas o resto antes de inserir vírgula no quociente)

Raiz quadrada e cúbica

A**(1/2) : Raiz quadrada
A**(1/3) : Raiz cúbica                                   '''

''' Ordem de Precedência

1 - Parêntesese

2 - Potenciação

3 - Multiplicação, divisão, divisão inteira, e resto de divisão inteira (o que vier primeiro no cálculo)

4 - Adição e subtração (o que vier primeiro no cálculo)                                              '''

# Exemplo de operação utilizando operadores aritméticos

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
pot = n1 ** n2
mult = n1 * n2
div = n1 / n2
divint = n1 // n2
divrest = n1 % n2
sum = n1 + n2
sub = n1 - n2

# É possível limitar as casas decimais colocando ":.2f" dentro da máscara. No exemplo anterior, teriamos 2 casas decimais. O 'f' é de float.
# Para evitar a quebra de linha entre um print e outro, colocar `end=''` no fim do print anterior.
print(f'A potência é {pot:.2f}, o produto é {mult:.2f}, a divisão é {div:.2f}', end=', ')
print(f'A divisão inteira é {divint}, o resto é {divrest:.2f}, a soma é {sum:.2f}, a subtração é {sub:.2f}')

''' Em .format():
print('a potência é {:.2f}, o produto é {:.2f}, a divisão é {:.2f}'.format(pot, mult, div), end=', ')
print('a divisão inteira é {}, o resto é {:.2f}, a soma é {:.2f}, a subtração é {:.2f}'.format(divint, divrest, sum, sub)) '''




#########################
### Outros operadores ###
#########################


''' Operadores de atribuição

A = B : A recebe o valor B
A += B : Incremento de B em A
A -= B : Decremento de B em A
A *= B : Multiplicação de A por B
A /= B : Divisão de A por B	
A %= B : Resto da divisão de A por B atribuído a A	'''


''' Operadores de comparação

A > B : A é maior que B  
A < B : A é menor que B  
A == B : A é igual a B (atenção: == compara, = atribui!)  
A != B : A é diferente de B  
A >= B : A é maior ou igual a B  
A <= B : A é menor ou igual a B '''


''' Operadores lógicos, de identidade e de associação

# Operadores lógicos
A and B : A e B são verdadeiros (só é True se ambos forem True)  
A or B : A ou B é verdadeiro (é True se pelo menos um for True)  
not (A) : Negação de A (inverte: True vira False, e vice-versa)  

# Operadores de identidade
A is B : A e B são o mesmo objeto na memória (comparação de identidade, não de valor)  
A is not B : A e B não são o mesmo objeto na memória  

# Operadores de associação 
A in B : A está contido em B (ex: elemento em lista, caractere em string. Segue a lógica de OR, ou seja, é 'True' se QUALQUER conteúdo em B for 'True') 
A not in B : A não está contido em B (Segue a lógica de AND, ou seja, é 'True' se NENHUM conteúdo em B for 'True'.)

IMPORTANTE!!! 'is' ≠ '==' : '==' compara valores, 'is' compara identidade (mesmo endereço de memória). '''


''' Formatação de posicionamento em máscara

":número" - Define quantidade de espaço na máscara.
":>" - Alinhar a variável à direita do espaço.
":<" - Alinhar a variável à esquerda do espaço.
":^" - Alinhar a variável ao centro do espaço. '''

print(f'{'1':20}') # Strings ficam à esquerda dos espaços por padrão.
print(f'{1:20}') # Números ficam à direita dos espaços por padrão.

nome = input("Digite seu nome: ")

''' É possível também preencher os espaços que sobram com um caractere. 
Abaixo coloquei a letra "x" para ficar no lugar dos espaços, e configurei para a variável ficar centralizada dentro dos 20 espaços. '''
print(f'Bem-vindo, {nome:x^20}!.\nAproveite os estudos!')


''' Caracteres de escape

\n - Nova linha = Quebra o texto para a próxima linha.
		
\t - Tabulação = Adiciona um espaço de tabulação.
	
\r - Retorno = Move o cursor para o início da linha, muito útil para laços de repetição. 

\'texto' = Serve para transformar caracteres especiais em strings. '''
