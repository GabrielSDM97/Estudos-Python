# Desafio 21

# Crie a classe Caneta, que simula o funcionamento de uma caneta colorida,
# podendo escrever frases na cor relativa.

from rich import print
from rich.traceback import install
install()


class Caneta:
    
    def __init__(self, cor=" "):
        self.cor = "blue" if cor == "azul" else "yellow" if cor == "amarelo" else "white"
        self.destampada = False

    def destampar(self):
        if (self.destampada == False):
            print(f"[{self.cor}]Caneta[/] pronta para uso!\n")
        else:
            print(f"[{self.cor}]Caneta[/] já está destampada!\n")
        self.destampada = True

    def escrever(self, conteudo=" "):
        print(f"Destampe a [{self.cor}]caneta[/] primeiro!\n") if self.destampada == False else print(
              f"[{self.cor}]{conteudo}[/]", end=" ")

    def quebrar_linha(self, quebras=" "):
        print(quebras * "\n", end="")


caneta1 = Caneta("azul")
caneta2 = Caneta("amarelo")

caneta1.escrever("Teste1")
caneta2.escrever("Teste2")

caneta1.destampar()
caneta2.destampar()
caneta1.destampar()
caneta2.destampar()

caneta1.escrever("Olá mundo!")
caneta2.escrever("Tudo bem?")
caneta1.quebrar_linha(2)
caneta1.escrever("Vamos estudar!")
caneta2.escrever("Foco!")
caneta1.quebrar_linha(1)
