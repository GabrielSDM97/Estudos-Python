from bebidas import *
from rich.traceback import install
install()


def main():
    bebida1 = Cafe()
    bebida2 = Cha()
    bebida3 = Leite()
    bebida1.preparar()
    bebida2.preparar()
    bebida3.preparar()


if __name__ == "__main__":
    main()
