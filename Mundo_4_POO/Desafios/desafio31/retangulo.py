from rich import print
from rich.traceback import install
install()


class Retangulo:
    def __init__(self, base: int|float = 1, altura: int|float = 1):
        # Atributos de instância
        self._base = None
        self._altura = None
        self._area = None

        # Atributos validáveis. Muito mais seguro!
        self.base = base
        self.altura = altura

    def validar_valor(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError("Os valores informados devem ser numéricos!")
        if valor < 0:
            raise ValueError("Os valores numéricos informados devem ser positivos!")

    @property
    def base(self) -> int|float:
        return self._base

    @base.setter
    def base(self, base: int|float):
        self.validar_valor(base)
        self._base = base

    @property
    def altura(self) -> int|float:
        return self._altura

    @altura.setter
    def altura(self, altura: int|float):
        self.validar_valor(altura)
        self._altura = altura

    @property
    def area(self) -> int|float:
        self._area = self._base * self._altura
        return self._area

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
