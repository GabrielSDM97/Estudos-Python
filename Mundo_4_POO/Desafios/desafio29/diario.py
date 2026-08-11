from rich.traceback import install
install()


class Diario:
    def __init__(self, senha="CeV!@"):
        self.__segredos = list()
        self.__senha = senha

    @property
    def senha(self):
        raise PermissionError("Ninguém pode ver a senha!")

    def escrever(self, msg: str) -> None:
        self.__segredos.append(f"Linha {len(self.__segredos) + 1} - {msg}")

    def ler(self, senha=None) -> str:
        if senha != self.__senha:
            raise PermissionError("Senha inválida!")
        return f"[green bold]Diário desbloqueado:[/]\n{"\n".join(self.__segredos)}"
