from rich.traceback import install
install()

class Termostato:
    def __init__(self):
        self.__temperatura = 24

    @property
    def temperatura(self) -> float:
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, temp: float):
        if temp % 0.5 != 0:
            raise ValueError(f"Temperatura {temp} é inválida!")
        self.__temperatura = 16 if temp < 16 else 30 if temp > 30 else temp

    @property
    def ftemperatura(self) -> str:
        return f"{self.__temperatura} {chr(176)}C"
