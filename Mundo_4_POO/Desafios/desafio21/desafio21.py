# Desafio 21

# Crie a classe Caneta, que simula o funcionamento de uma caneta colorida,
# podendo escrever frases na cor relativa.

from rich import print
from rich.traceback import install
install()


class Caneta:
    
    def __init__(self, cor:str="azul"):
        self.cor = "red" if cor == "vermelho" else "yellow" if cor == "amarelo" else "green" if cor == "verde" else "azul"
        self.destampada = False

    def tampar(self) -> None:
        self.destampada = False

    def destampar(self) -> None:
        self.destampada = True

    def escrever(self, conteudo:str=" ") -> None:
        destampar_aviso = f"\nDestampe a [{self.cor}]caneta[/] primeiro!\n"
        texto = f"[{self.cor}]{conteudo}[/]"
        print(destampar_aviso if self.destampada == False else texto, end="")

    def quebrar_linha(self, quebras:int=1) -> None:
        print(quebras * "\n", end="")


caneta1 = Caneta("vermelho")
caneta2 = Caneta("amarelo")
caneta3 = Caneta("verde")

caneta1.escrever("_")
caneta1.destampar()
caneta2.destampar()
caneta3.destampar()

caneta1.escrever("Olá mundo!")
caneta1.tampar()
caneta1.escrever("_")
caneta1.destampar()
caneta2.escrever("Tudo bem?")
caneta3.quebrar_linha(1)
caneta3.escrever("Vamos estudar!")
caneta3.quebrar_linha(2)
