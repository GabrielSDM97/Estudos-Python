from aluno import Aluno
from rich import print, inspect
from rich.traceback import install
install()


# Regras do sistema
# 1. Anos de nascimento devem ser entre 1926 e 2026
# 2. Proibido inserir idade diretamente via método "self.idade"
# 3. Não é possível cadastrar um aluno em um curso inexistente
# 4. É possível cadastrar um novo curso com self.addcurso("curso")
# desde que o curso tenha pelo menos 2 caracteres e que não já exista na lista.

def main():
    a = Aluno("José", 2000, "ADS")

    # Erro 1 - Inserir ano anterior a 1926 ou após 2026
    try:
        a.nascimento = 1925
    except ValueError as ve:
        print(f"[red bold]{ve.__class__.__name__}[/]: {ve}")

    # Erro 2 - Proibido inserir idade diretamente.
    try:
        a.idade = 10
    except PermissionError as pe:
        print(f"[red bold]{pe.__class__.__name__}[/]: {pe}")

    # Erro 3 - Cadastrar aluno em curso inexistente
    try:
        a.curso = "ADM"
    except ValueError as ve:
        print(f"[red bold]{ve.__class__.__name__}[/]: {ve}")

    # Erro 4 - Cadastrar curso com nome inválido (menor que 2 caracteres)
    try:
        a.add_curso("A")
    except ValueError as ve:
        print(f"[red bold]{ve.__class__.__name__}[/]: {ve}")

    # Erro 5 - Cadastrar curso já existente
    try:
        a.add_curso("ADS")
    except ValueError as ve:
        print(f"[red bold]{ve.__class__.__name__}[/]: {ve}")

    # Adicionando curso corretamente, evitando o Erro 4 e 5!
    a.add_curso("ADM")
    # Alterando o curso do aluno para um curso existente, evitando o Erro 3!
    a.curso = "ADM"

    inspect(a, private=True, methods=True)


if __name__ == "__main__":
    main()
