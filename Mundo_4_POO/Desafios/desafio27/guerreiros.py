from personagem import Personagem
from random import randint, choice
from time import sleep
from rich import print
from rich.traceback import install
install()


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["soco leve", "soco pesado",
                       "chute leve", "chute pesado"]

    def curar(self):
        cura = randint(1, 100)
        self.vida += cura
        print(
            f"\n[yellow bold]{self.nome}[/] fez uma atadura e recuperou [green bold]{cura}[/] de vida ficando com [bold]{self.vida}[/] de vida!")
        sleep(0.5)


class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["invocação", "conjuração de fogo",
                       "conjuração de gelo", "conjuração elétrica"]

    def curar(self):
        cura = randint(1, 100)
        self.vida += cura
        print(f"\n[yellow bold]{self.nome}[/] fez uma magia e recuperou [green bold]{cura}[/] de vida ficando com [bold]{self.vida}[/] de vida!")
        sleep(0.5)
