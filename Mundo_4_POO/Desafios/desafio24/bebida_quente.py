from abc import ABC, abstractmethod
from rich.traceback import install
install()


class BebidaQuente(ABC):

    @abstractmethod
    def servir(self):
        pass

    @abstractmethod
    def misturar(self):
        pass

    def ferver_agua(self):
        print("1. Fervendo água a 100 graus Célsius.")

    def preparar(self):
        print(f"\n--- Iniciando Preparo de {self.__class__.__name__} ---")
        self.ferver_agua()
        self.misturar()
        self.servir()
