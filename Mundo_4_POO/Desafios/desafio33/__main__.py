from aluno import Aluno
from rich import print, inspect
from rich.traceback import install
install()


# Regras do sistema
# 1. Anos de nascimento devem ser entre 1926 e 2026
# 2. Proibido inserir idade diretamente via método "self.idade"
# 3. Não é possível cadastrar um aluno em um curso inexistente

def main():
    try:
        a1 = Aluno("José", 2000, "ADM")
        inspect(a1, private=True, methods=True)
    except ValueError as ve:
        print(f"[red bold]{ve.__class__.__name__}[/]: {ve}")
    

    # Erro 1 - Inserir ano anterior a 1926 ou após 2026
    try:
        a1.nascimento = 1925
        inspect(a1, private=True, methods=True)
    except ValueError as ve:
        print(f"[red bold]{ve.__class__.__name__}[/]: {ve}")

    # Erro 2 - Proibido inserir idade diretamente.
    try:
        a1.idade = 10
    except PermissionError as pe:
        print(f"[red bold]{pe.__class__.__name__}[/]: {pe}")

    # Erro 3 - Cadastrar aluno em curso inexistente
    try:
        a1.curso = "ADM"
    except ValueError as ve:
        print(f"[red bold]{ve.__class__.__name__}[/]: {ve}")

    # Adicionando curso
    a1.add_curso("ADM")
    # Agora o Erro 3 não ocorre, já que o curso ADM foi adicionado com o método "add_curso()".
    a1.curso = "ADM"
    inspect(a1, private=True, methods=True)


if __name__ == "__main__":
    main()
