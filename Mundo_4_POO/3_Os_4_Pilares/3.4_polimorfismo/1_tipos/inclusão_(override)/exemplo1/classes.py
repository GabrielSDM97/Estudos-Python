from rich.traceback import install
install()


class Animal():
    def __init__(self, nome: str):
        self.nome = nome

    def fazer_som(self):
        print(f"{self.nome} fez um som!\n")


# Herda tudo da classe mãe "Animal", ou seja, qualquer método aqui é MONOMÓRFICO
class Galinha(Animal):
    pass


# Herda tudo da classe mãe "Animal", ou seja, qualquer método aqui é MONOMÓRFICO
class Pato(Animal):
    pass


# Herda tudo da classe mãe "Animal", ou seja, qualquer método aqui é MONOMÓRFICO
class Gato(Animal):
    pass


class Cachorro(Animal):

    def fazer_som(self):  # Sobrescreve/override o método "fazer_som" da classe mãe "Animal", ou seja, esse método é POLIMÓRFICO
        print(f"{self.nome} acabou de fazer 'AUAUAU!'\n")


class Spitz(Cachorro):

    def fazer_som(self):  # Sobrescreve/override o método "fazer_som" da classe mãe "Cachorro", ou seja, esse método é POLIMÓRFICO
        print(f"{self.nome} acabou de fazer 'au!au!au!au!au!'\n")


class Pitbull(Cachorro):

    def fazer_som(self):  # Sobrescreve/override o método "fazer_som" da classe mãe "Cachorro", ou seja, esse método é POLIMÓRFICO
        print(f"{self.nome} acabou de fazer 'HUF HUF HUF!'\n")
