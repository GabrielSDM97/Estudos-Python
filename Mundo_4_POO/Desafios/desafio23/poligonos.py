from poligono import Poligono
from rich.traceback import install
from math import pi
install()


class Circulo(Poligono):

    def __init__(self, raio = 1):
        super().__init__(0)
        self.raio = raio

    def __str__(self):
        return f"Círculo de raio {self.raio} cm"

    def area(self):
        return (self.raio ** 2) * pi

    def perimetro(self):
        return (pi * self.raio) * 2


class Quadrado(Poligono):
    def __init__(self, lado = 1):
        super().__init__(4)
        self.lado = lado

    def __str__(self):
        return f"Quadrado de lado {self.lado} cm"

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return self.qtd_lados * self.lado
