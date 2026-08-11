from abc import ABC
from rich.traceback import install
install()


class Pessoa(ABC):
    def __init__(self, nome, nascimento):
        self._nome = nome
        self._nascimento = nascimento if 1926 <= nascimento <= 2026 else None

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, nascimento):
        if nascimento < 1926 or nascimento > 2026:
            raise ValueError("Ano de nascimento inválido!")
        self._nascimento = nascimento

    @property
    def idade(self):
        return 2026 - self._nascimento

    @idade.setter
    def idade(self, idade):
        raise PermissionError("Você não pode alterar a idade. Mude o ano de nascimento!")
