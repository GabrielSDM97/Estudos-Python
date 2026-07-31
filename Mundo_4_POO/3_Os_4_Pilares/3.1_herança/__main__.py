from subclasses import *
from rich import inspect
from rich.traceback import install
install()

def main():
    a1 = Aluno("Gabriel", 18, "ADS", "ADS1")
    a1.fazer_aniversario()
    a1.fazer_matricula()
    # inspect(a1, methods = True)

    p1 = Professor("Maria", 28, "Professora", "Mestrado")
    p1.fazer_aniversario()
    p1.dar_aula()
    # inspect(p1, methods = True)

    f1 = Funcionario("Roberto", 18, "Secretária", "Admnistrativo")
    f1.fazer_aniversario()
    f1.bater_ponto()
    # inspect(f1, methods = True)

# Previne que a função main() deste arquivo seja importada em outros arquivos,
# limitando a execução dela apenas a este arquivo.
if __name__ == "__main__":
    main()
