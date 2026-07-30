''' Tratamento de Erros e Exceções '''

## NameError - Erro de sintaxe ##

# primt(x) # A sintaxe 'primt' não existe, o correto seria 'print()'


## NameError - Erro de significado (semântico) ##

# print(x) # A variável x não existe


## ValueError - Exceção por inserir valor de tipo primitivo errado ##

# num = int('x')


## ZeroDivionByZero - Execeção por dividir um número por 0 ##

# num = 4/0


## TypeError - Erro de tipo ##

# num = 4/'2'


## IndexError - Índice fora de range (Todo array inicia-se no índice/posição 0) ##

# lst=[1,2,3]
# print(lst[3])


## ModuleNotFoundError - Módulo não encontrado ##

# import moduloteste


''' Existem muitos outros tipos de exceptions (exceções), e, para evitar que um erro quebre o programa, 
utilizamos a estrutura 'try...except...else...finally' '''

try:
    a = int(input('Digite o 1º número: '))
    b = int(input('Digite o 2º número: '))
    r = a/b
except (ValueError, TypeError):
    print(f'Tivemos um problema com os tipos de dados inseridos!')
except ZeroDivisionError:
    print(f'Você tentou dividir por 0!')
except KeyboardInterrupt:
    print(f'Você tentou finalizar sem inserir nenhum dado!')
except Exception as erro: # Para outros tipos de exceções não especificadas acima
    print(f'Tivemos o erro de classe {erro.__class__} e causa {erro.__cause__}!')
else:
    print(f'O resultado é {r:.1f}')
finally: # É sempre executado, tanto faz se for depois de 'else' ou 'except'.
    print('Até logo')

# Dica: Sempre inicie os testes com valores corretos.

# IMPORTANTE!!! O 'finally' SEMPRE será executado, mesmo que seja posicionado depois de um 'return' em uma função ou depois de um 'break' em um laço de repetição.
