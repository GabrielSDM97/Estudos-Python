from rich.traceback import install
install()


class Mae:
    def __init__(self, nome:str = "Mamãe"):
        self.nome = nome

    def fazer_pudim(self):
        print(f"{self.nome} faz pudim com LEITE e CALDO!\n")

    def fazer_coxinha(self):
        print(f"{self.nome} faz coxinha com FRANGO e QUEIJO!\n")


class Filho(Mae):

    # Continua herdando "fazer_coxinha" (Monomórfico)

    # Mas "fazer_pudim" abaixo sobrescreve/override o da classe mãe (Polimórfico)
    def fazer_pudim(self):
        print(f"{self.nome} faz pudim com MEL e CHOCOLATE!\n")


class Filha(Mae):

    # Continua herdando "fazer_pudim" (Monomórfico)

    # Mas o "fazer_coxinha" abaixo sobrescreve/override o da classe mãe (Polimórfico)
    def fazer_coxinha(self):
        print(f"{self.nome} faz coxinha com CARNE e CHEDDAR!\n")
