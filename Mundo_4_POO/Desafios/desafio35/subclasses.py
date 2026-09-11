from superclasse import Arquivo
from rich import print
from rich.traceback import install
install()


class PDF(Arquivo):
    def __init__(self, nome, tamanho):
        super().__init__(nome, tamanho, "pdf")

    def abrir(self):
        return f"Abrindo {self.nome_completo} com Adobe Reader!"


class DOC(Arquivo):
    def __init__(self, nome, tamanho):
        super().__init__(nome, tamanho, "docx")

    def abrir(self):
        return f"Abrindo {self.nome_completo} com Libre Office!"


class PNG(Arquivo):
    def __init__(self, nome, tamanho):
        super().__init__(nome, tamanho, "png")

    def abrir(self):
        return f"Abrindo {self.nome_completo} com Photo Viewer!"


def abrir_arquivo(self):
    try:
        print(self.abrir())
    except Exception as ex:
        print(f"[red bold]{ex.__class__.__name__}[/]: {ex}")
