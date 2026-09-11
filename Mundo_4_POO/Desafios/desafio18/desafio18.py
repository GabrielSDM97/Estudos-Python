# Desafio 18

# Crie a classe Churrasco, onde seja possível informar quantas pessoas
# vão participar e mostre quanto de carne deve ser comprado, o custo total
# do churrasco e o preço por pessoa.

# Consumo padrão: 400g por pessoa
# Preço: R$82,40/kg

from rich import print
from rich.panel import Panel
from rich.traceback import install
install()


class Churrasco:
    preco_kg: float = 82.4
    consumo_pessoa_kg: float = 0.4

    def __init__(self, titulo: str = " ", convidados: int = 0):
        self.titulo: str = titulo
        self.convidados: int = convidados

    def __str__(self) -> str:
        return f"Calcula despezas do churrasco {self.titulo} com {self.convidados} convidados!"

    def peso_carne(self) -> float:
        return self.convidados * Churrasco.consumo_pessoa_kg

    def custo_total(self) -> float:
        return self.peso_carne() * Churrasco.preco_kg

    def preco_por_pessoa(self) -> float:
        return self.custo_total() / self.convidados

    def analise(self) -> None:
        conteudo = f"Analisando [chartreuse1]{self.titulo}[/] com [bright_cyan]{self.convidados} convidados[/].\n"
        conteudo += f"Cada participante comerá [yellow]{Churrasco.consumo_pessoa_kg}KG[/] e cada KG custa [yellow]R${Churrasco.preco_kg}[/].\n"
        conteudo += f"Recomendo comprar [orange4]{self.peso_carne():,.2f}KG[/] de carne.\n"
        conteudo += f"O custo total será de [red]R${self.custo_total():,.2f}[/].\n"
        conteudo += f"Cada pessoa pagará [green]R${self.preco_por_pessoa():,.2f}[/] para participar.\n"
        painel = Panel(conteudo, title=self.titulo, width=70)
        print(painel)


churras1 = Churrasco("Churras dos amigos 1", 15)
print(churras1)
churras1.analise()

churras2 = Churrasco("Churras dos amigos 2", 80)
print(churras2)
churras2.analise()
