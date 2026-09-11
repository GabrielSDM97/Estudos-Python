from abc import ABC, abstractmethod
from rich.traceback import install
install()


class Arquivo(ABC):
    def __init__(self, nome, tamanho, extensao):
        self.nome = nome
        self._extensao = extensao
        self.tamanho = tamanho/1000000

    @property
    def nome_completo(self):
        return f"'{self.nome}.{self._extensao}' ({self.tamanho})MB"

    def abrir(self):
        return f"Abrindo {self.nome_completo} com Undefined!"
