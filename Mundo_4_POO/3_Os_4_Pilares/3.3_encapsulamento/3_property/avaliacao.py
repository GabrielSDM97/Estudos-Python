from rich import print
from rich.traceback import install
install()


class Avaliacao:
    def __init__(self, nome, disciplina, nota=0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota  # Atributo protegido (#)

    # Criando Atributo Validável
    @property
    def nota(self):  # Getter
        return self._nota

    @nota.setter
    def nota(self, valor):  # Setter
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print("[red]Nota inválida[/]")

    @nota.deleter
    def nota(self):  # Condição para excluir uma nota
        pass
