from rich import print
from rich.traceback import install
install()


class Numero:
    def __init__(self, valor: int | float = 0):
        self.valor = valor

    def dobrar(self):
        self.valor *= 2

    def __str__(self):
        return f"Tenho o valor {self.valor} dentro de {self.__class__.__name__}!"


class Texto:
    def __init__(self, valor: str = 0):
        self.texto = valor

    def dobrar(self):
        self.texto += " " + self.texto

    def __str__(self):
        return f"Tenho o texto '{self.texto}' dentro de {self.__class__.__name__}!"


class Papel:
    def __init__(self):
        self.dobrado = False

    def dobrar(self):
        self.dobrado = True

    def __str__(self):
        return f"O papel está {'DOBRADO' if self.dobrado else 'NOVO'}!"

class Lista:
    def __init__(self, lista: list = list()):
        self.lista = lista

    def dobrar(self):
        self.lista += self.lista

    def __str__(self):
        return f"Tenho os itens: {self.lista}"


class Casa:
    def __init__(self):
        pass

    def __str__(self):
        return f"Era uma casa, muito engraçada..."


# Método Pythônico Polimórfico (Duck-Typing)
def tentar_dobrar(objeto):
    try:
        objeto.dobrar()
    except:
        print(f"[red bold]Encontrei problemas ao tentar dobrar [green]{objeto.__class__.__name__}[/][/]!")
