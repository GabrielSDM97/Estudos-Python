from hashlib import sha256
from rich.traceback import install
install()


class Credencial:
    def __init__(self):
        self.__hash = None

    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self, senha: str):
        self.__hash = sha256(senha.encode()).hexdigest()

    def validar(self, senha: str) -> str:
        senhaTemp = sha256(senha.encode()).hexdigest()
        if senhaTemp != self.__hash:
            raise PermissionError("Senha inválida!")
        return "[green bold]Senhas iguais![/]"

