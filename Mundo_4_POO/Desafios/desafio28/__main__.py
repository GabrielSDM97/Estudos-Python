from termostato import Termostato
from rich import inspect, print
from rich.traceback import install
install()


# Regras do sistema
# 1. O sitema aceita apenas valores múltiplos de 0.05.
# 2. Temperaturas válidas: entre 16 e 30. 
# 3. Temperatura padrão: 24.

def main():
    t = Termostato()

    while True:
        try:
            t.temperatura = float(input("Temperatura: "))
        except ValueError as ve:
            print(f"[red bold]{ve.__class__.__name__}[/]: {ve}")

        print(f"\nTemperatura: {t.ftemperatura} / {t.temperatura}\n")
        inspect(t, private=True, methods=True)

        continuar = str(input("Testar nova temperatura? [S/N] ").strip()[0])
        if continuar in "Nn": break


if __name__ == "__main__":
    main()
