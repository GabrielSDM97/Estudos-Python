from superclasse import Pessoa
from rich import print
from rich.traceback import install
install()


# Classes especializadas (especialização) / Subclasses

# Aluno É UMA Pessoa
class Aluno(Pessoa):  # class NomeClasse(Superclasse) - Herda métodos
    def __init__(self, nome: str, idade: int, curso: str, turma: str):
        # super() = Função que permite chamar métodos da superclasse a partir de suas subclasses.
        # Abaixo a função "super()" está chamando o método construtor da superclasse.
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self) -> None:
        print(f"[blue]{self.nome}[/] de {self.idade} anos acabou de fazer matrícula no curso {self.curso} na turma {self.turma}!")


# Professor É UMA Pessoa
class Professor(Pessoa):
    def __init__(self, nome: str, idade: int, especialidade: str, nivel: str):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self) -> None:
        print(f"[yellow]{self.nome}[/] de {self.idade} anos, {self.especialidade} com {self.nivel}, acabou de dar aula!")


# Funcionário É UMA Pessoa
class Funcionario(Pessoa):
    def __init__(self, nome: str, idade: int, cargo: str, setor: str):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self) -> None:
        print(f"[green]{self.nome}[/] de {self.idade} anos trabalha de {self.cargo} no setor {self.setor} e acabou de bater ponto!")
