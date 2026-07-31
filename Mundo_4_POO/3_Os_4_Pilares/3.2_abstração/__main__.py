from subclasses import *
from rich import inspect
from rich.traceback import install
install()

def main():
    a1 = Aluno("Gabriel", 17, "Ensino Médio", "Turma 1")
    a1.fazer_aniversario()
    a1.fazer_matricula()
    a1.estudar()
    # inspect(a1, methods = True)

    p1 = Professor("Roberto", 28, "Matemática", "Mestrado")
    p1.fazer_aniversario()
    p1.dar_aula()
    p1.estudar()
    # inspect(p1, methods = True)

    f1 = Funcionario("Maria", 25, "Secretária", "Administrativo")
    f1.fazer_aniversario()
    f1.bater_ponto()
    f1.estudar()
    # inspect(f1, methods = True)

if __name__ == "__main__":
    main()
