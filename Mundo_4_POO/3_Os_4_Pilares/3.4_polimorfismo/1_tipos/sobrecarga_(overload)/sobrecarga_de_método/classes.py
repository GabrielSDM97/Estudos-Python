from functools import singledispatchmethod
from rich.traceback import install
install()

# @singledispatchmethod
# Decorador que permite criar métodos de sobrecarga.
# O despacho é feito APENAS pelo PRIMEIRO argumento após self,
# desconsiderando quaisquer outros parâmetros inseridos após ele.


class Analisador:

    @singledispatchmethod
    def analisar(self, valor): # Método base (sem @register): é o FALLBACK para tipos não registrados.
        print(f"Não foi possível analisar o valor {valor}")

    @analisar.register
    def _(self, valor: int): # O typehint em métodos @register funciona como filtro.
        print(f"O valor {valor} é inteiro!")

    @analisar.register
    def _(self, valor: float):
        print(f"O valor {valor} é float!")

    @analisar.register
    def _(self, valor: str):
        print(f"O valor {valor} é uma cadeia de caracteres (string)!")

    @analisar.register
    def _(self, valor: bool):
        print(f"O valor {valor} é booleano!")

    @analisar.register # União de tipos: será chamado se qualquer um deles for detectado.
    def _(self, valor: tuple | list | dict):
        print(f"O valor {valor} é uma coleção de dados!")
