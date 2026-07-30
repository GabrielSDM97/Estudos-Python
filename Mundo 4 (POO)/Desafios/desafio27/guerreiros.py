from personagem import Personagem
from random import randint
from time import sleep
from rich import print
from rich.traceback import install
install()


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def curar(self):
        cura = randint(1, 100)
        self.vida += cura
        print(f"\n[yellow bold]{self.nome}[/] fez uma atadura e curou [green bold]{cura}[/] de vida ficando com [bold]{self.vida}[/] de vida!")
        sleep(1)


class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def curar(self):
        cura = randint(1, 100)
        self.vida += cura
        print(f"\n[yellow bold]{self.nome}[/] fez uma magia e curou [green bold]{cura}[/] de vida ficando com [bold]{self.vida}[/] de vida!")
        sleep(1)
