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
        self.misturar()

    def preparar(self):
        print("\n--- Iniciando Preparo ---")
        self.ferver_agua()
