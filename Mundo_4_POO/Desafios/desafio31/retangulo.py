from rich import print
from rich.traceback import install
install()


class Retangulo:
    def __init__(self, base: float, altura: float):
        self._base = base if base >= 0 else 0
        self._altura = altura if altura >= 0 else 0
        self._area = self._base * self._altura

    def validacao(self, valor):
        if valor < 0:
            raise ValueError("Valor negativo!")

    @property
    def area(self) -> float:
        return self._area

    @area.setter
    def area(self, area: tuple() = (0, 0)):
        self._area = area[0] * area[1]

    @property
    def base(self) -> float:
        return self._base

    @base.setter
    def base(self, base: float):
        self.validacao(base)
        self._base = base
        self.area = (base, self._altura)

    @property
    def altura(self) -> float:
        return self._altura

    @altura.setter
    def altura(self, altura: float):
        self.validacao(altura)
        self._altura = altura
        self.area = (self._base, altura)

    @property
    def medidas(self):
        return (f"\nBase: {self._base:.2f}"
                f"\nAltura: {self._altura:.2f}"
                f"\nÁrea: {self._area:.2f}")

    @medidas.setter
    def medidas(self, medidas: tuple() = (0, 0)):
        self.base = medidas[0]
        self.altura = medidas[1]
