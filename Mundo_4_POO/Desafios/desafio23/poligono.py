from abc import ABC, abstractmethod
from rich.traceback import install
install()


class Poligono(ABC):
    def __init__(self, qtd_lados: int = 1):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self) -> float:
        pass

    @abstractmethod
    def area(self) -> float:
        pass
