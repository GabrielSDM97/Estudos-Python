from abc import ABC, abstractmethod
from random import randint
from time import sleep
from rich import print
from rich.traceback import install
install()


class Personagem(ABC):
    def __init__(self, nome, vida, golpe = 0):
        self.nome = nome
        self.vida = vida
        self.golpe = golpe

    def receber_dano(self, atacante, dano):
        self.vida -= dano
        if self.vida <= 0: 
            print(f"\n[yellow bold]{self.nome}[/] foi [red bold]derrotado[/] por [yellow bold]{atacante.nome}[/] ao receber [red bold]{dano}[/] de dano! [red bold italic]GAME OVER![/]")
            quit()
        print(f"\n[yellow bold]{self.nome}[/] recebeu [red bold]{dano}[/] de dano ficando com [bold]{self.vida}[/] de vida!")
        sleep(1)

    def atacar(self, alvo, forca):
        self.golpe = randint(1, forca)
        print(f"\n[yellow bold]{self.nome}[/]([bold]{self.vida}[/]) atacou [yellow bold]{alvo.nome}[/]([bold]{alvo.vida}[/]) com golpe de força {forca}!")
        sleep(1)
        alvo.receber_dano(self, self.golpe)

    @abstractmethod
    def curar(self):
        pass
