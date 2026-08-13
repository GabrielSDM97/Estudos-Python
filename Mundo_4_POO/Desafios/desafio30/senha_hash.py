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
    def senha(self, novaSenha: str):
        if len(novaSenha.strip()) <= 0:
            raise ValueError("A senha deve ter pelo menos 1 caractere!")
        self.__hash = sha256(novaSenha.encode("utf-8")).hexdigest()

    def validar(self, senhaUsuario: str) -> str:
        hashTemp = sha256(senhaUsuario.encode("utf-8")).hexdigest()
        if hashTemp != self.__hash:
            raise PermissionError("Senha inválida!")
        return "[green bold]Senha correta![/]"
