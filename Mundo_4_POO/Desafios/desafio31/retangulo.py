from rich import print
from rich.traceback import install
install()


class Retangulo:
    def __init__(self, base: float = 1, altura: float = 1):
        # Atributos de instância
        self._base = None
        self._altura = None
        self._area = None

        # Atributos validáveis
        self.base = base
        self.altura = altura

    def validacao(self, valor):
        if not isinstance(valor, (float, int)):
            raise TypeError("Os valores informados devem ser numéricos!")
        if valor < 0:
            raise ValueError("Os valores numéricos informados devem ser positivos!")

    @property
    def base(self) -> float:
        self._area = self._base * self._altura
        return self._area

    @base.setter
    def base(self, base: float):
        self.validacao(base)
        self._base = base

    @property
    def altura(self) -> float:
        return self._altura

    @altura.setter
    def altura(self, altura: float):
        self.validacao(altura)
        self._altura = altura

    @property
    def area(self) -> float:
        return self._base * self._altura

    @area.setter
    def area(self, area: tuple):
        raise PermissionError("A área não pode ser alterada diretamente!")

    @property
    def medidas(self) -> str:
        return (f"\nBase: {self.base:,.2f}"
                f"\nAltura: {self.altura:,.2f}"
                f"\nÁrea: {self.area:,.2f}")

    @medidas.setter
    def medidas(self, medidas: tuple):
        if not isinstance(medidas, tuple):
            raise TypeError("As medidas devem ser informadas em uma tupla!")
        if len(medidas) != 2:
            raise SyntaxError("Informe uma tupla com apenas 2 valores numéricos!")
        self.base = medidas[0]
        self.altura = medidas[1]
