# Desafio 17

# Crie a classe Produto, onde podemos cadastro nome e o preço.
# Crie também um método que mostre uma etiqueta de preço do produto.

from rich import print
from rich.panel import Panel
from rich.traceback import install
install()


class Produto:

    def __init__(self, nome: str = " ", preço: float = 0):
        self.nome: str = nome
        self.preço: float = preço

    def etiqueta(self) -> "Panel":
        conteudo = (self.nome).center(28, " ")
        conteudo += f"\n{28 * "-"}"
        conteudo += f"R${self.preço:,.2f}".center(28, ".")
        etiqueta = Panel(conteudo, title="Produto", width=32, style="grey0 on yellow1")
        return etiqueta


produto1 = Produto("iPhone 17 Pro Max", 25000.85)
produto2 = Produto("Mouse", 120)

print(produto1.etiqueta())
print(produto2.etiqueta())
