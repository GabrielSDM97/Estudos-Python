''' Modularização

Serve para reduzir o código do programa principal e guardar funções rotineiras dentro de um módulo.

Benefícios:

- Torna o código mais legível

- Facilita a manutenção

- Melhor organização do código

- Reutilização dos mesmos códigos em outros projetos

- Ocultação de código detalhado '''


''' Pacotes

Quando apenas um módulo já não é suficiente por conta do tamanho do projeto, é ai que entra os pacotes.

Um módulo é um arquivo .py com funções reutilizáveis.

Um pacote é uma pasta com diversos outros pacotes ou módulos, facilitando ainda mais a organização.

IMPORTANTE! Todo pacote deve ter o arquivo "__init__.py" dentro dele, no qual ficarão as funções que serão importadas e reutilizadas. '''


# Exemplo
from uteis import matemática

num = int(input('Fatorial: '))
fat = matemática.fatorial(num)
print(f'O fatorial de {num} é {fat}!')
print(f'O dobro é {matemática.dobro(num)}!')
print(f'O triplo é {matemática.triplo(num)}!')
