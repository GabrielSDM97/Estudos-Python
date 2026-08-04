from avaliacao import Avaliacao
from rich import inspect
from rich.traceback import install
install()


def main():
    aluno1 = Avaliacao("Maurício", "Matemática", 10)
    print(aluno1.nota)

    aluno1.nota = 3.5
    print(aluno1.nota)

    aluno1.nota = 999
    print(aluno1.nota)

    # Parâmetro 'private = True' mostra atributos privados.
    inspect(aluno1, private=True, methods=True)

if __name__ == "__main__":
    main()
