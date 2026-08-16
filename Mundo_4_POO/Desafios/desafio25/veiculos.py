from transporte import Transporte
from rich import print
from rich.traceback import install
install()


class Moto(Transporte):
    fator = 0.5

    def calc_frete(self):
        self.frete = self.distancia * Moto.fator
        return f"[green bold]R${self.frete:,.2f}[/]"


class Caminhao(Transporte):
    fator = 1.2
    dist_min = 50

    def calc_frete(self):
        self.frete = self.distancia * Caminhao.fator if self.distancia >= Caminhao.dist_min else 0
        return f"[green bold]R${self.frete:,.2f}[/]" if self.frete else "Distância abaixo do limite mínimo de [red bold]50KM[/]!"


class Drone(Transporte):
    fator = 9.5
    dist_max = 10

    def calc_frete(self):
        self.frete = self.distancia * Drone.fator if self.distancia <= Drone.dist_max else 0
        return f"[green bold]R${self.frete:,.2f}[/]" if self.frete else "Distância acima do limite máximo de [red bold]10KM[/]!"
