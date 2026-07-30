from rich import print
# A classe "Table" permite a criação de tabelas (colunas e linhas).
from rich.table import Table

tabela = Table(title="Minha tabela")
tabela.add_column("Nome", justify="center", style="green")
tabela.add_column("Idade", justify="center", style="yellow")
tabela.add_row("Maria", "32")
tabela.add_row("José", "42")
tabela.add_row("Roberto", "20")
tabela.add_row("Laura", "[red]200[/]")

print(tabela)
