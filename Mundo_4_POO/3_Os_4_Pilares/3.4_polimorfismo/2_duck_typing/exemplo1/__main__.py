from classes import *
from rich.traceback import install
install()


def main():
    obj1 = Porta()
    obj2 = Empresa()
    obj3 = Ovo()
    obj4 = Pedra()

    tentar_abrir(obj1)
    tentar_abrir(obj2)
    tentar_abrir(obj3)
    tentar_abrir(obj4)


if __name__ == "__main__":
    main()
