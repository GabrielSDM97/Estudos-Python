# Desafio 16

# Crie a classe Funcionario, onde podemos cadastrar
# nome, setor e cargo. Crie também um método que permita ao
# funcionário se apresentar.

from rich import print
from rich.table import Table
from rich import inspect
from rich.traceback import install
install()


class Funcionario:
    empresa:str = "Curso em Vídeo"

    def __init__(self, nome:str=" ", setor:str=" ", cargo:str=" "):
        self.nome:str = nome
        self.setor:str = setor
        self.cargo:str = cargo

    def apresentacao(self) -> str:
        return f"\nOlá :waving_hand:, meu nome é [green]{self.nome}[/] :smiling_face_with_smiling_eyes:. Sou [yellow]{self.cargo}[/] no setor de [blue]{self.setor}[/] e trabalho na empresa [red]{self.__class__.empresa}[/]!\n"


cadastro1 = Funcionario("Maria", "cosméticos", "vendedora")
print(cadastro1.apresentacao())

cadastro2 = Funcionario("José", "finanças", "contador")
print(cadastro2.apresentacao())

# inspect(Funcionario)
