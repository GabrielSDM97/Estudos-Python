# Para criar um arquivo utiliza-se a função 'open()'
# Abrindo um arquivo chamado 'Arquivo1.txt'.
a = open('Arquivo1.txt', 'wt') 
# Fecha o arquivo, sendo possível acessá-lo/modificá-lo apenas se for aberto novamente com 'open(...)'.
a.close() 

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

# Exemplo:
try:
    b = open('Arquivo2.txt', 'xt+')
except:
    print('\'\nArquivo2.txt\' já criado!\n')
else:
    print('\'\nArquivo2.txt\' criado com sucesso!\n')
    # O método '.write()' serve para inserir UMA string no arquivo.
    b.write('Abc;\nBca;\nCba;\n')
    # O método '.writelines()' serve para inserir MÚLTIPLAS strings no arquivo.
    b.writelines(['Teste1;\n', 'Teste2;\n', 'Teste3;\n']) 

b = open('Arquivo2.txt', 'rt')
print('1º - \n', end='')
# O método '.read()' mostra todo o conteúdo em string a partir da posição do cursor só que em string. O conteúdo aparece como ele é.
print(b.read()) 
# O método '.seek(n)' serve para mudar a posição do cursor dentro do arquivo. O valor '0' volta o cursor para o início do arquivo.
b.seek(0) 
print('2º - \n', end='')
# O método '.readlines()' mostra todo o conteúdo de um arquivo a partir da posição do cursor só que em lista. Cada linha se torna um elemento desta lista.
print(b.readlines()) 
''' O método ".readlines()" também pode ser utilizado para copiar o conteúdo transformado em lista de um arquivo para uma variável, 
    Exemplo: "variavel = arquivo.readlines()" '''

b.close()

print()

# Existe também a estrutura 'with' que, automaticamente, fecha um arquivo aberto após a execução da estrutura, sem a necessidade de utilizar '.close()'
# Exemplo:
with open('Arquivo3.txt', 'wt+') as arquivo:
    arquivo.write('Olá\nComo vai?!')
    arquivo.seek(0)
    # É possível ver o conteúdo de um arquivo, linha por linha, em um laço de repetição. O cursor sofre alteração de posição aqui também.
    for linha in arquivo:
        print(f'3º {linha.replace('\n','')}')
    arquivo.seek(0)

    # CURIOSIDADE!!!
    # Não é possível ver todo o conteúdo de um arquivo direto em uma print, mostrando apenas os metadados do objeto em si.
    print(f"\n4º {arquivo}") 
    conteudoArquivo = arquivo.readlines()
    # Já após uma cópia com 'readlines()' é possível ver o conteúdo do arquivo transformado em lista.
    print(f"\n5º {conteudoArquivo}\n") 

# Prova real de que o arquivo foi fechado.
try:
    arquivo.read()
except Exception as erro:
    print(f'\nO erro {erro.__class__.__name__} comprova que o arquivo \'Arquivo3.txt\' de fato foi fechado após o fim da estrutura \'with\' :D!')
finally:
    print('\nAté logo!')

# IMPORTANTE (Dica sobre posição de cursor)
''' Após utilizar qualquer método de leitura ou escrita, o cursor se move para uma posição específica no arquivo, exemplos:
Modo leitura: O cursor começa no início do arquivo, indo para o fim do arquivo quando ocorrer uma leitura com o método 'obj.read()'.
Modo escrita: O cursor começa no fim do arquivo.
Para voltar com o cursor para o início do arquivo, usa-se o método 'obj.seek(0)'. '''

# Removendo arquivos
from os import remove

for i in range(1,4):
    remove(f'Arquivo{i}.txt')
