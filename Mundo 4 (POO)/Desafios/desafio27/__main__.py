from guerreiros import *
from rich.traceback import install
install()


def main():
    guerreiro1 = Guerreiro("Mario", 200)
    guerreiro2 = Mago("Koopa", 200)
    round = 1

    while True:
        print(f"\nRound {round}: ")
        guerreiro1.atacar(guerreiro2, 100)
        guerreiro1.curar()
        round += 1
        print(f"\nRound {round}: ")
        guerreiro2.atacar(guerreiro1, 100)
        guerreiro2.curar()
        round += 1
        

if __name__ == "__main__":
    main()
