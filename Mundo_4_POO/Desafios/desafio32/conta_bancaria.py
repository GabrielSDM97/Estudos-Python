from hashlib import sha256
from getpass import getpass
from rich.traceback import install
install()


class ContaBancaria:
    def __init__(self, id: int, titular: str, saldo: float, chave: str = None):
        self._id = id
        self._titular = titular
        self.__saldo = saldo
        self.__hash = sha256(chave.encode()).hexdigest() if chave else sha256(self.pede_senha().encode()).hexdigest()

    def __str__(self):
        return f"Saldo atual: R${self.__saldo}"

    @property
    def nome(self) -> str:
        return self._titular

    @nome.setter
    def nome(self, nome: str):
        if self.validar_senha(self.pede_senha()):
            self._titular = nome

    def validar_senha(self, chave: str) -> bool:
        hashChave = sha256(chave.encode()).hexdigest()
        return bool(hashChave == self.__hash)

    def pede_senha(self) -> str:
        chave = getpass("Senha: ")
        return chave

    def sacar(self, valor: float, chave: str = None) -> str:
        chave = self.pede_senha() if chave == None else chave
        if self.validar_senha(chave):
            valor = abs(valor)
            if valor > self.__saldo:
                raise ValueError("Saldo insuficiente!\n")
            self.__saldo -= valor
            return f"Saque de [green bold]R${valor:,.2f}[/] efetuado com sucesso!\n"
        raise PermissionError("Senha inválida! Saque não autorizado!\n")

    def depositar(self, valor: float) -> str:
        valor = abs(valor)
        self.__saldo += valor
        return f"Depósito de [green bold]R${valor:,.2f}[/] efetuado com sucesso!\n"
