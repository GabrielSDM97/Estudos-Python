from rich import print
from rich.traceback import install
install()

class Termostato:
    def __init__(self):
        self.__temperatura = 24

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, temperatura):
        try:
            if temperatura % 0.5 != 0:
                raise ValueError(f"ERRO! Temperatura {temperatura} é inválida!")
        except ValueError as ve:
            print(f"[red]{ve}[/]")
        else:
            if temperatura < 16:
                self.__temperatura = 16
            elif temperatura > 30:
                self.__temperatura = 30
            else:
                self.__temperatura = temperatura

    @property
    def ftemperatura(self):
        return f"[yellow]{self.__temperatura}[/] °C"
