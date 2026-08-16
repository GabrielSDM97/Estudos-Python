from classes import *
from rich.traceback import install
install()


def main():
    x = Analisador()
    
    x.analisar(1)
    x.analisar(9.5)
    x.analisar("Olá")
    x.analisar(True)
    x.analisar({"A":1})
    x.analisar(None)


if __name__ == "__main__":
    main()
