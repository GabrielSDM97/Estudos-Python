from classes import *
from rich.traceback import install
install()


def main():
    a = Numero(10)
    b = Texto("Olá")
    c = Papel()
    d = Lista([1,2,3])
    e = Casa()

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print()

    tentar_dobrar(a)
    tentar_dobrar(b)
    tentar_dobrar(c)
    tentar_dobrar(d)
    tentar_dobrar(e)

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)


if __name__ == "__main__":
    main()
