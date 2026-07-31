from cargos import *
from rich import print
from rich.traceback import install
install()


def main():
    func1 = Horista("José", 12, 200)
    func1.calc_sal()
    print(func1.analisar_sal())

    func2 = Mensalista("Maria", 9500)
    func2.calc_sal()
    print(func2.analisar_sal())


if __name__ == "__main__":
    main()
