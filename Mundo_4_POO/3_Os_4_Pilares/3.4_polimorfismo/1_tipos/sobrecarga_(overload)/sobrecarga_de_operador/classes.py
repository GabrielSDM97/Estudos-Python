from rich.traceback import install
install()


class Carteira:
    def __init__(self, valor: int | float = 0):
        self.__saldo = valor

    def __str__(self):
        return f"Você tem R${self.__saldo:,.2f} na carteira!"

    # Equal to ( == )
    def __eq__(self, outro: object) -> bool:
        return bool(self.__saldo == outro.__saldo)

    # In-place addition ( += )
    def __iadd__(self, valor: int|float) -> object:
        self.__saldo += valor
        return self

    # In-place substraction ( -= )
    def __isub__(self, valor: int|float) -> object:
        self.__saldo -= valor
        return self

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor: int | float):
        raise PermissionError("Você não pode inserir um saldo diretamente!")
