# Para criar um arquivo utiliza-se a função 'open()'

a = open('Arquivo1.txt', 'wt') # Abrindo um arquivo chamado 'Arquivo1.txt'.
a.close() # Fecha o arquivo, sendo possível acessá-lo/modificá-lo apenas se for aberto novamente com 'open(...)'.

''' 
O segundo parâmetro da função 'open()' define o 'modo' que será utilizado para tratar do arquivo.

----- Modos -----
r - Leitura (read) - Abre para leitura.
w - Escrita (write) - Cria um novo arquivo ou sobrescreve se já existir.
x - Criação exclusiva (write) - Cria um novo arquivo. Falha se o arquivo já existir (útil para evitar sobrescrita acidental).
a - Adição (write) - Abre para escrita. O cursor começa ao final do arquivo (não apaga o conteúdo anterior). Cria o arquivo se não existir.
r+ - Adiciona escrita (write). O cursor começa no início do arquivo.
w+ ou x+ ou a+ - Adiciona leitura (read).
------------------
É possível utilizar 't' (texto padrão) ou 'b' (binário) juntamente com o modo, exemplo: (xt), (rb+), etc...
'''

# Exemplo
try:
    b = open('Arquivo2.txt', 'xt+')
except:
    print('\'\nArquivo2.txt\' já criado!\n')
else:
    print('\'\nArquivo2.txt\' criado com sucesso!\n')
    b.write('Abc;\nBca;\nCba;\n') # O método '.write()' serve para inserir UMA string no arquivo.
    b.writelines(['Teste1;\n', 'Teste2;\n', 'Teste3;\n']) # O método '.writelines()' serve para inserir MÚLTIPLAS strings no arquivo.

b = open('Arquivo2.txt', 'rt')
print('1º - \n', end='')
print(b.read()) # O método '.read()' mostra o conteúdo em string. O conteúdo aparece como ele é.
b.seek(0) # O método '.seek(n)' serve para mudar a posição do cursor dentro do arquivo.
print('2º - ', end='')
print(b.readlines()) # O método '.readlines()' mostra o conteúdo de um arquivo em lista. Cada linha se torna um elemento desta lista.

b.close()

print()


# Existe também a estrutura 'with' que, automaticamente, fecha um arquivo aberto após a execução da estrutura, sem a necessidade de utilizar '.close()'
# Exemplo
with open('Arquivo3.txt', 'wt+') as arquivo:
    arquivo.write('Olá\nComo vai?!')
    arquivo.seek(0)
    for linha in arquivo:
        print(f'{linha.replace('\n','')}')

# Prova real de que o arquivo foi fechado.
try:
    arquivo.read()
except Exception as erro:
    print(f'\nO erro {erro.__class__.__name__} comprova que o arquivo \'Arquivo3.txt\' de fato foi fechado após o fim da estrutura \'with\' :D!')
finally:
    print('\nAté logo!')

# IMPORTANTE (Dica sobre posição de cursor)
''' Após utilizar qualquer metodo de leitura ou escrita, o cursor se movimenta para a posição definida no parâmetro, no caso de um metodo de leitura, ou
para o fim do arquivo, caso seja um metodo de escrita ou um metodo de leitura sem um parâmetro definido, ou seja, caso você queira fazer 
novas consultas do começo do arquivo, utilize o método 'obj.seek(0)' para que o cursor volte para o início. '''

# Removendo arquivos
from os import remove

for i in range(1,4):
    remove(f'Arquivo{i}.txt')
