from classes import *
from rich.traceback import install
install()


def main():
    a1 = Galinha("Bandit")
    a2 = Pato("Frajola")
    a3 = Gato("Garfield")
    a4 = Cachorro("Lulu")
    c1 = Spitz("Destruidor de mundos")
    c2 = Pitbull("Florzinha")

    a1.fazer_som()
    a2.fazer_som()
    a3.fazer_som()
    a4.fazer_som()
    c1.fazer_som()
    c2.fazer_som()


if __name__ == "__main__":
    main()
