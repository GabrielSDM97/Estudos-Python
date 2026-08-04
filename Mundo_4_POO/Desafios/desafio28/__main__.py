from termostato import Termostato
from rich import print
from rich import inspect
from rich.traceback import install
install()


def main():
    termo = Termostato()
    termo.temperatura = 25
    print(f"\nTemperatura: {termo.ftemperatura} / {termo.temperatura}\n")
    inspect(termo, private=True, methods=True)  

    # Inserindo valor inválido
    termo.temperatura = 25.2

if __name__ == "__main__":
    main()
