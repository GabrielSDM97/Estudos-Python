from os import system
from guerreiros import *
from rich import inspect
from rich.traceback import install
install()


def main():
    guerreiro1 = Guerreiro("Tyr", 100)
    guerreiro2 = Mago("Draven", 100)
    round = 1

    while True:
        system("clear")
        print(f"\nRound {round}: ")
        guerreiro1.atacar(guerreiro2, 150)
        guerreiro2.curar()
        guerreiro2.atacar(guerreiro1, 150)
        guerreiro1.curar()
        guerreiro1.status()
        guerreiro2.status()
        sleep(10)
        round += 1
        

if __name__ == "__main__":
    main()
