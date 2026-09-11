from hashlib import sha256
from rich import print
from rich.traceback import install
install()


class ContaBancaria:
    def __init__(self, id: int, titular: str, saldo: int|float, chave: str = None):
        self._id = id
        self._titular = titular
        self.__saldo = saldo
        self.__hash = sha256(chave.encode("utf-8")).hexdigest() if chave else sha256(self.pede_senha().encode("utf-8")).hexdigest()
        print(f"Conta {self._id} criada com sucesso! Saldo atual de [green bold]R${self.__saldo:,.2f}[/]")

    def __str__(self):
        return f"Saldo atual da conta {self._id}: R${self.__saldo:,.2f}"

    def validar_senha(self, chave: str) -> bool:
        hash_chave = sha256(chave.encode("utf-8")).hexdigest()
        return bool(hash_chave == self.__hash)

    def pede_senha(self) -> str:
        from pwinput import pwinput
        while True:
            chave = str(pwinput("Senha: ", mask = "*")).strip()
            if len(chave) >= 6:
                break
            print("[red bold]Erro![/] A senha deve ter pelo menos 6 dígitos. Tente novamente!")
        return chave

    def sacar(self, valor: int|float, chave: str = None) -> str:
        if valor > self.__saldo:
            raise ValueError("Saldo insuficiente!\n")    
        chave = self.pede_senha() if chave == None else chave
        if self.validar_senha(chave):
            valor = abs(valor)
            self.__saldo -= valor
            return f"Saque de [green bold]R${valor:,.2f}[/] efetuado com sucesso!\n"
        raise PermissionError("Senha inválida! Saque não autorizado!\n")

    def depositar(self, valor: int|float) -> str:
        valor = abs(valor)
        self.__saldo += valor
        return f"Depósito de [green bold]R${valor:,.2f}[/] efetuado com sucesso!\n"

    @property
    def nome(self) -> str:
        return self._titular

    @nome.setter
    def nome(self, nome: str):
        if self.validar_senha(self.pede_senha()) == False:
            raise PermissionError("Senha inválida! Troca de titular não autorizada!\n")
        self._titular = nome
