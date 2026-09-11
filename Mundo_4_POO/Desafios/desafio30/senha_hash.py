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
    def senha(self, nova_senha: str):
        if len(nova_senha.strip()) <= 0:
            raise ValueError("A senha deve ter pelo menos 1 caractere!")
        self.__hash = sha256(nova_senha.encode("utf-8")).hexdigest()

    def validar(self, senha_usuario: str) -> str:
        hash_temp = sha256(senha_usuario.encode("utf-8")).hexdigest()
        if hash_temp != self.__hash:
            raise PermissionError("Senha inválida!")
        return "[green bold]Senha correta![/]"
