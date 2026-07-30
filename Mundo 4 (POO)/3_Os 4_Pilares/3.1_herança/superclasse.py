from rich.traceback import install
install()

# Classe genérica (generalização) / Superclasse
class Pessoa:
    def __init__(self, nome:str = "", idade:int = 0):
        self.nome = nome
        self.idade = idade
    def fazer_aniversario(self, idade:int=0):
        self.idade += 1
