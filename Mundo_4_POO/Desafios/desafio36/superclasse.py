from abc import ABC, abstractmethod
from rich.traceback import install
install()


class Pagamento(ABC):
    def __init__(self):
        self._valor = None

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    # Serve apenas para retornar o valor monetário formatado
    @property
    def fvalor(self):
        from currencies_lib import BRL
        return BRL(self._valor)

    @abstractmethod
    def pagar(self, valor: float):
        pass
