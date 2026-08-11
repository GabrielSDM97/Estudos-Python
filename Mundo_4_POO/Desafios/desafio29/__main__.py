from diario import Diario
from rich import inspect, print
from rich.traceback import install
install()


# Regras do sistema
# 1. A senha para ler o diário deve ser a mesma definida durante a instanciação.
# 2. Caso não seja definida nenhuma senha, a senha padrão é: CeV!@

def main():
    diario = Diario()

    while True:
        diario.escrever(str(input("Mensagem: ")))

        inspect(diario, private=True, methods=True)

        try:
            print(f"\n{diario.ler(str(input("Senha: ")))}")
        except PermissionError as pe:
            print(f"\n[red bold]{pe.__class__.__name__}[/]: {pe}")

        continuar = str(input("\nEscrever mais? [S/N] ").strip()[0])
        if continuar in "Nn": break


if __name__ == "__main__":
    main()
