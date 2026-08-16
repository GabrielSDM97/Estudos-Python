from classes import *
from rich.traceback import install
install()


def main():
    p1 = Mae("Jussara")
    p2 = Filho("Roberto")
    p3 = Filha("Maria")

    p1.fazer_pudim()
    p1.fazer_coxinha()
    p2.fazer_pudim()
    p2.fazer_coxinha()
    p3.fazer_pudim()
    p3.fazer_coxinha()

if __name__ == "__main__":
    main()
