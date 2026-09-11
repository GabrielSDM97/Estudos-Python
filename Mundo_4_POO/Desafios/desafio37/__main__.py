from rich import print
from rich.panel import Panel
from rich.traceback import install
install()

class Mensagem():
    def __init__(self, mensagem, tipo = "AVISO", icone = ":thought_balloon:"):
        self._mensagem = mensagem
        self._tipo = tipo
        self._icone = icone

    def mostrar(self):
        print(Panel.fit(self._mensagem, title = f"{self._icone} {self._tipo} {self._icone}", padding=(1, 3)))


class Erro(Mensagem):
    def __init__(self, mensagem):
        super().__init__(mensagem, "ERRO", ":cross_mark:")

    def mostrar(self):
        print(Panel.fit(self._mensagem, title = f"{self._icone} {self._tipo} {self._icone}", style="yellow on red", padding=(1, 3)))


class Alerta(Mensagem):
    def __init__(self, mensagem):
        super().__init__(mensagem, "ALERTA", ":warning:")

    def mostrar(self):
        print(Panel.fit(self._mensagem, title = f"{self._icone} {self._tipo} {self._icone}", style="red on yellow", padding=(1, 3)))


def main():
    # Instanciando objeto temporário/anônimo.
    Mensagem("Mensagem!").mostrar()
    Alerta("Mensagem!").mostrar()
    Erro("Mensagem!").mostrar()

if __name__ == "__main__":
    main()
