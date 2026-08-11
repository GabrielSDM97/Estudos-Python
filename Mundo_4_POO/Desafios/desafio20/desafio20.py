# Desafio 20

# Crie a classe Gamer, onde podemos cadastrar nome, nick e jogos favoritos de uma pessoa.
# Cria também um método que permita mostrar a ficha desse gamer.

from rich import print
from rich.panel import Panel
from rich.traceback import install
install()


class Gamer:

    def __init__(self, nome: str = " ", nick: str = " "):
        self.nome: str = nome
        self.nick: str = nick
        self.jogosFavoritos: list = list()

    def add_jogo_favorito(self, jogo: str = " ") -> None:
        self.jogosFavoritos.append(f":video_game: [purple]{jogo}[/]")

    def ficha_jogador(self) -> None:
        conteudo = f"Nome real: [yellow]{self.nome}[/]\n"
        favoritos = "\n".join(sorted(self.jogosFavoritos, key=str.lower))
        conteudo += f"Jogos favoritos:\n{favoritos}"
        titulo = f"Jogador <[green]{self.nick}[/]>"
        ficha = Panel.fit(conteudo, title=titulo)
        print(ficha)


jogador1 = Gamer("Gabriel", "Biéu")
jogador1.add_jogo_favorito("Medal of Honor")
jogador1.add_jogo_favorito("Mount & Blade Bannerlord")
jogador1.add_jogo_favorito("Stellaris")
jogador1.add_jogo_favorito("Arena Breakout Infinite")
jogador1.ficha_jogador()
