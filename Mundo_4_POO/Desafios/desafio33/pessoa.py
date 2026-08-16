from datetime import date
from rich.traceback import install
install()


class Pessoa():
    def __init__(self, nome: str, nascimento: int):
        self._nome = nome
        self._nascimento = None
        self.nascimento = nascimento

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, nascimento):
        if nascimento < 1926 or nascimento > date.today().year:
            raise ValueError("Ano de nascimento inválido!")
        self._nascimento = nascimento

    @property
    def idade(self):
        return date.today().year - self._nascimento

    @idade.setter
    def idade(self, idade):
        raise PermissionError("Você não pode alterar a idade. Mude o ano de nascimento!")
