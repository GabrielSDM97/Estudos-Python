from senha_hash import Credencial
from rich import inspect, print
from rich.traceback import install
install()


# Regras do sistema
# 1. A senha de validação deve ser a mesma definida em "cred.senha".

def main():
    cred = Credencial()
    
    inspect(cred, private=True, methods=True)

    while True:
        cred.senha = str(input("Nova senha: "))

        try:
            print(cred.validar(str(input("Senha para validação: "))))
        except PermissionError as pe:
            print(f"[red bold]{pe.__class__.__name__}[/]: {pe}")

        continuar = str(input("Deseja continuar? [S/N] ").strip()[0])
        if continuar in "Nn": break


if __name__ == "__main__":
    main()
