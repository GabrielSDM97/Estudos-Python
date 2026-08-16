from abc import ABC, abstractmethod
from random import randint, choice
from time import sleep
from rich import print
from rich.panel import Panel
from utils.mp3player import mp3
from rich.traceback import install
install()


class Personagem(ABC):
    def __init__(self, nome, vida: int, golpes: list = list()):
        self.nome = nome
        self.vida = vida
        self.golpes = golpes

    def receber_dano(self, atacante: "Personagem", dano: int) -> None:
        self.vida -= dano
        if self.vida <= 0:
            print(f"\n[yellow bold]{self.nome}[/] foi [red bold]derrotado[/] por [yellow bold]{atacante.nome}[/] ao receber [red bold]{dano}[/] de dano! \n\n\t\t   [red bold italic]GAME OVER![/]\n")
            mp3("sons/game_over.mp3")
            quit()
        print(f"\n[yellow bold]{self.nome}[/] recebeu [red bold]{dano}[/] de dano ficando com [bold]{self.vida}[/] de vida!")
        sleep(0.5)

    def atacar(self, alvo: "Personagem", forca: int) -> None:
        golpe = f"[salmon1 bold]{choice(self.golpes)}[/]"
        print(f"\n[yellow bold]{self.nome}[/]([bold]{self.vida}[/]) atacou [yellow bold]{alvo.nome}[/]([bold]{alvo.vida}[/]) com golpe {golpe} de força {forca}!")
        sleep(0.5)
        alvo.receber_dano(self, randint(1, forca))
    
    def status(self):
        conteudo = f"Nome: [yellow bold bold]{self.nome}[/]\n"
        conteudo += f"Vida: [green bold]{self.vida}[/]\n"
        conteudo += f"Classe: [dark_magenta bold]{self.__class__.__name__}[/]\n"
        conteudo += f"Golpes: [salmon1 bold]{" [white]-[/] ".join(self.golpes)}[/]"
        painelStats = Panel.fit(conteudo, title=f"Status")
        print(painelStats)

    @abstractmethod
    def curar(self) -> None:
        pass

