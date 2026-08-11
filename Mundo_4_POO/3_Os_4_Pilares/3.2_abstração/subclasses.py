from superclasse import Pessoa
from rich import print
from rich.traceback import install
install()

# Classes concretas


class Aluno(Pessoa):
    def __init__(self, nome: str, idade: int, curso: str, turma: str):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self) -> None:
        print(f"[blue]{self.nome}[/] de {self.idade} anos acabou de fazer matrícula no curso {self.curso} na turma {self.turma}!")

    def estudar(self) -> None:
        print(f"[blue]{self.nome}[/] está estudando matérias do curso {self.curso}!")


class Professor(Pessoa):
    def __init__(self, nome: str, idade: int, especialidade: str, nivel: str):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self) -> None:
        print(f"[yellow]{self.nome}[/] de {self.idade} anos, {self.especialidade} com {self.nivel}, acabou de dar aula!")

    def estudar(self) -> None:
        print(f"[yellow]{self.nome}[/] está estudando para lecionar {self.especialidade}!")


class Funcionario(Pessoa):
    def __init__(self, nome: str, idade: int, cargo: str, setor: str):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self) -> None:
        print(f"[green]{self.nome}[/] de {self.idade} anos trabalha de {self.cargo} no setor {self.setor} e acabou de bater ponto!")

    def estudar(self) -> None:
        print(f"[green]{self.nome}[/] está estudando assuntos do setor {self.setor}!")
