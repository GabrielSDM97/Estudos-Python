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
    precoKG = 82.4
    consumoPessoaKG = 0.4

    def __init__(self, titulo=" ", convidados=0):
        self.titulo = titulo
        self.convidados = convidados

    def __str__(self):
        return f"Calcula despezas do churrasco {self.titulo} com {self.convidados} convidados!"

    def peso_carne(self) -> float:
        return self.convidados * Churrasco.consumoPessoaKG

    def custo_total(self) -> float:
        return self.peso_carne() * Churrasco.precoKG

    def preco_por_pessoa(self) -> float:
        return self.custo_total() / self.convidados

    def analise(self):
        conteudo = f"Analisando [chartreuse1]{self.titulo}[/] com [bright_cyan]{self.convidados} convidados[/].\n"
        conteudo += f"Cada participante comerá [yellow]{Churrasco.consumoPessoaKG}KG[/] e cada KG custa [yellow]R${Churrasco.precoKG}[/].\n"
        conteudo += f"Recomendo comprar [orange4]{self.peso_carne():,.2f}KG[/] de carne.\n"
        conteudo += f"O custo total será de [red]R${self.custo_total():,.2f}[/].\n"
        conteudo += f"Cada pessoa pagará [green]R${self.preco_por_pessoa():,.2f}[/] para participar.\n"
        painel = Panel(conteudo, title=self.titulo, width = 70)
        print(painel)

churras1 = Churrasco("Churras dos amigos", 15)
print(churras1)
churras1.analise()

churras1 = Churrasco("Churras dos amigos", 80)
print(churras1)
churras1.analise()
