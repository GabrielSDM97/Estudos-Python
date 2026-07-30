from abc import ABC, abstractmethod
from rich.traceback import install
install()


class Transporte(ABC):
    def __init__(self, distancia, frete = 0):
        self.distancia = distancia
        self.frete = frete

    @abstractmethod
    def calc_frete(self):
        pass
