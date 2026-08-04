from avaliacao import Avaliacao
from rich.traceback import install
install()


def main():
    aluno1 = Avaliacao("Maurício", "Matemática", 10)
    print(aluno1.get_nota())
    
    aluno1.set_nota(100)
    print(aluno1.get_nota())

if __name__ == "__main__":
    main()
