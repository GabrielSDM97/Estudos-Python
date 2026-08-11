from pessoa import Pessoa
from rich.traceback import install
install()


class Aluno(Pessoa):
    cursos_oficiais = ["ADS", "SI"]

    def __init__(self, nome, nasc, curso=None):
        super().__init__(nome, nasc)
        self._curso = curso if curso in Aluno.cursos_oficiais else None

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso):
        if curso not in Aluno.cursos_oficiais:
            raise ValueError(f"Curso {curso} não está na lista!")
        self._curso = curso

    def add_curso(self, curso: str):
        Aluno.cursos_oficiais.append(curso)
