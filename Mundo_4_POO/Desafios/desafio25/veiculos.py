from transporte import Transporte
from rich import print


class Moto(Transporte):
    fator = 0.5

    def __init__(self, distancia):
        super().__init__(distancia, distancia * Moto.fator)

    def __str__(self):
        return f"[yellow bold]{self.distancia}[not bold]KM[/][/]"

    def calc_frete(self):
        return f"[green]R${self.frete:,.2f}[/]"


class Caminhao(Transporte):
    fator = 1.2

    def __init__(self, distancia):
        super().__init__(distancia, distancia * Caminhao.fator if distancia >= 50 else 0)

    def __str__(self):
        return f"[yellow bold]{self.distancia}[not bold]KM[/][/]"

    def calc_frete(self):
        return f"[green]R${self.frete:,.2f}[/]" if self.frete != 0 else "Distância abaixo do limite mínimo de [red]50KM[/]!"


class Drone(Transporte):
    fator = 9.5

    def __init__(self, distancia):
        super().__init__(distancia, distancia * Drone.fator if distancia <= 10 else 0)

    def __str__(self):
        return f"[yellow bold]{self.distancia}[not bold]KM[/][/]"

    def calc_frete(self):
        return f"[green]R${self.frete:,.2f}[/]" if self.frete != 0 else "Distância acima do limite máximo de [red]10KM[/]!"
