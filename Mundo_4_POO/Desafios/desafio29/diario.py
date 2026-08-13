from rich.traceback import install
install()


class Diario:
    def __init__(self, senha="CeV!@"):
        self.__segredos = list()
        self.__senha = senha.strip()

    @property
    def senha(self):
        raise PermissionError("Ninguém pode ver a senha!")

    @senha.setter
    def senha(self, senha):
        validarSenha = str(input("Senha antiga: ")).strip()
        if validarSenha != self.__senha:
            raise PermissionError("Senha inválida!")
        self.__senha = senha

    def escrever(self, msg: str) -> None:
        # isinstance - Verifica se a instância do parâmetro "msg" é string. 
        if isinstance(msg, str) and len(msg) > 0:
            self.__segredos.append(f"{msg.strip()}")

    def ler(self, senha=None) -> str:
        if senha != self.__senha:
            raise PermissionError("Senha inválida!")
        return f"[green bold]Diário desbloqueado:[/]\n{"\n".join(self.__segredos)}"
