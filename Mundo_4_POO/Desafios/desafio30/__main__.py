from senha_hash import Credencial
from rich import inspect, print
from rich.traceback import install
install()


# Regras do sistema
# 1. Uma senha deve ter pelo menos 1 caracatere.
# 2. A senha de validação deve ser a mesma atribuida ao atributo validável "self.senha".

def main():
    cred = Credencial()

    while True:
        try:
            cred.senha = str(input("Nova senha: "))
        except ValueError as ve:
            print(f"[red bold]{ve.__class__.__name__}[/]: {ve}")

        inspect(cred, private=True, methods=True)

        if cred.senha:
            try:
                print(cred.validar(str(input("Senha para validação: "))))
            except PermissionError as pe:
                print(f"[red bold]{pe.__class__.__name__}[/]: {pe}")

        continuar = str(input("Deseja continuar? [S/N] ").strip()[0])
        if continuar in "Nn": break


if __name__ == "__main__":
    main()
