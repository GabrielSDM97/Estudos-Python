from pessoa import Pessoa
from rich.traceback import install
install()


class Aluno(Pessoa):
    cursos_oficiais = ["ADS", "SI"]

    def __init__(self, nome: str, nasc: int, curso: str = None):
        super().__init__(nome, nasc)
        self._curso = None
        self.curso = curso

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso):
        if curso not in Aluno.cursos_oficiais:
            raise ValueError(f"Curso {curso} não está na lista!")
        self._curso = curso

    def add_curso(self, curso: str):
        if curso.strip() in Aluno.cursos_oficiais:
            raise ValueError(f"Curso {curso} já existe na lista!")
        if len(curso.strip()) <= 2:
            raise ValueError("Padrão inválido para cursos")
        Aluno.cursos_oficiais.append(curso)
