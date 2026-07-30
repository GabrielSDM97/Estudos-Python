from poligono import Poligono
from rich.traceback import install
from math import pi
install()


class Circulo(Poligono):

    def __init__(self, qtd_lados: int):
        super().__init__(qtd_lados)

    def __str__(self):
        return f"Círculo de raio {self.qtd_lados}"

    def area(self) -> float:
        return pi * (self.qtd_lados ** 2)

    def perimetro(self) -> float:
        return 2 * (pi * self.qtd_lados)


class Quadrado(Poligono):
    def __init__(self, qtd_lados: int):
        super().__init__(qtd_lados)

    def __str__(self):
        return f"Quadrado de lado {self.qtd_lados}"

    def area(self) -> float:
        return self.qtd_lados ** 2

    def perimetro(self) -> float:
        return 4 * self.qtd_lados
