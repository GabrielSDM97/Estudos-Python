# Desafio 22

# Crie a classe ControleRemoto, onde vamos simular o funcionamento de um controle
# simples (canal, volume, e liga/desliga)

from rich import print
from rich.traceback import install
from rich.panel import Panel
install()


class ControleRemoto:
    
    def __init__(self):
        self.botao = " "
        self.status = " "
        self.power = 0
        self.volCima = 1
        self.volBaixo = 4
        self.listaCanais = ["[yellow on white] 1 [/]",
                            " 2 ", " 3 ", " 4 ", " 5 "]
        self.canal = 0

    def aumentar_volume(self):
        if (self.volCima < 5):
            self.volCima += 1
            self.volBaixo -= 1

    def diminuir_volume(self):
        if (self.volCima > 1):
            self.volCima -= 1
            self.volBaixo += 1

    def avancar_canal(self):
        self.listaCanais[self.canal] = f" {self.canal+1} "
        self.canal += 1 if self.canal < 4 else -4
        self.listaCanais[self.canal] = f"[yellow on white] {self.canal+1} [/]"

    def voltar_canal(self):
        self.listaCanais[self.canal] = f" {self.canal+1} "
        self.canal -= 1 if self.canal > 0 else -4
        self.listaCanais[self.canal] = f"[yellow on white] {self.canal+1} [/]"

    def status_tv(self):
        self.power = 1 if self.power == 0 else 0

    def hud_tv(self):
        while True:
            print(15 * "\n")
            if (self.power == 0):
                self.status = Panel.fit(
                    "[red]:prohibited: A TV está desligada[/]", title="[ TV ]")
            elif (self.power == 1):
                self.status = Panel.fit(
                    f"CANAL = {"".join(self.listaCanais)}\n"
                    f"VOLUME = {self.volCima * "[red on grey0] [/]"}{self.volBaixo * "[grey0 on white] [/]"}", title="[ TV ]")
            print(self.status)
            self.botao = str(
                input(f"< CH{self.canal+1} >\t - VOL{self.volCima} + "))
            match self.botao:
                case "@":
                    self.status_tv()
                case "+":
                    self.aumentar_volume()
                case "-":
                    self.diminuir_volume()
                case ">":
                    self.avancar_canal()
                case "<":
                    self.voltar_canal()
                case "0":
                    break
                case _:
                    print("[red]Opção inválida![/] Tente novamente.")


tv = ControleRemoto()
tv.hud_tv()

