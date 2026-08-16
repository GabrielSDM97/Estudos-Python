from classes import Carteira
from rich import print, inspect
from rich.traceback import install
install()


def main():
    c1 = Carteira(100)
    c2 = Carteira(200)

    print(c1 == c2) # c1.__eq__(c2)

    c1 += 200 # c1.__iadd__(200)
    
    print(c1)
    
    c1 -= 100 # c1.__isub__(100)

    print(c1)

if __name__ == "__main__":
    main()
