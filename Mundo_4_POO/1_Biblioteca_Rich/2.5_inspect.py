from rich import print
# A função inspect retorna, de forma organizada, o resultado do dunder "__doc__"
from rich import inspect

# Parâmetros de inspect()
# "all = True" - Mostra todos os atributos de um objeto.
# "methods = True" - Mostra todos os métodos de um objeto.
# "dunder = True" - Mostra todos os atributos dunders de um objeto. 
inspect(int, all=True) # Equivale a print(int.__doc__)

# Exemplo com uma simples classe:


class CadastroProduto:
    """
    Classe para cadastro de produtos.
    """

    def __init__(self, nome=" ", valor=0):
        self.nome = nome
        self.valor = valor


produto = CadastroProduto("Celular", 1000.00)

print(f"__doc:__{produto.__doc__}")
print("inspect:")
inspect(produto)
