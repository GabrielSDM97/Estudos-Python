# Desafio 19

# Crie a classe Livro, que vai simular a passagem de páginas de um livro,
# considerando também se o usuário chegou ao fim da leitura.

from rich import print
from rich.traceback import install
from time import sleep
install()


class Livro:
    
    def __init__(self, nome=" ", paginas=0):
        self.nome = nome
        self.fim = paginas
        self.paginaAtual = 1
        self.livroAberto = 0

        print(f"\n:book: Você acabou de abrir o livro \"[green]{self.nome}[/]\" que tem [steel_blue1]{self.fim} páginas[/] no total. "
              f"Você está na página {self.paginaAtual}!\n")

    def fim_do_livro(self) -> bool:
        return True if self.paginaAtual == self.fim else False

    def progresso_geral(self, quantidade) -> str:
        return f"Você avançou {quantidade} páginas. Agora está na página {self.paginaAtual}!\n"

    def progresso_atual(self) -> str:
        return f"[bold]Pg {self.paginaAtual}[/] >"

    def avancar_pagina(self, quantidade):
        if (quantidade <= 0):
            print("[bold red on grey0]Por favor, insira um valor positivo[/]\n")
            return
        contador = 0
        while contador < quantidade and not self.fim_do_livro():
            contador += 1
            self.paginaAtual += 1
            print(self.progresso_atual(), end = " ")
            sleep(0.15)
        print(self.progresso_geral(contador), end = " ")
        if (self.fim_do_livro()):
            print("\n[dodger_blue3]Fim do livro! :waving_hand:[/]\n")
            quit()
        

livro = Livro("A volta dos que não foram", 25)
livro.avancar_pagina(-1)
livro.avancar_pagina(5)
livro.avancar_pagina(10)
livro.avancar_pagina(20)
