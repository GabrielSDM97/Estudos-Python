from retangulo import Retangulo
from rich import inspect, print
from rich.traceback import install
install()


# Regras do sistema
# 1. O sistema apenas aceita números positivos

def main():
    try:
        ret = Retangulo(10, 20)
        print(ret.medidas)
    except ValueError as ve:
        print(f"[red bold]{ve.__class__.__name__}[/]: {ve}")

    try:
        ret.base = 20
        ret.altura = 40
        print(ret.medidas)
    except ValueError as ve:
        print(f"[red bold]{ve.__class__.__name__}[/]: {ve}")

    try:
        ret.medidas = (40, 80)
        print(ret.medidas)
    except ValueError as ve:
        print(f"[red bold]{ve.__class__.__name__}[/]: {ve}")

    # inspect(ret, private=True, methods=True)


if __name__ == "__main__":
    main()
