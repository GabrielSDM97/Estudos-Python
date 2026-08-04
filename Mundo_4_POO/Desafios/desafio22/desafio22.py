# Desafio 22

# Crie a classe ControleRemoto, onde vamos simular o funcionamento de um controle
# simples (canal, volume, e liga/desliga)

from os import system
from rich import print
from rich.traceback import install
from rich.panel import Panel
install()


class ControleRemoto:
    canalMin:int = 1
    volumeMin:int = 1
    canalMax:int = 5
    volumeMax:int = 5
 

    def __init__(self):
        self.ligado:bool = False
        self.volumeAtual:int = 1
        self.canalAtual:int = 1

    def hud_canais(self) -> str:
        canaisHud = ""
        for canal in range(ControleRemoto.canalMin, ControleRemoto.canalMax+1):
            canaisHud += f" {canal} " if self.canalAtual != canal else f"[grey0 on green1] {canal} [/]"
        return canaisHud

    def hud_volumes(self) -> str:
        volumeHud = ""
        for volume in range(ControleRemoto.volumeMin, ControleRemoto.volumeMax+1):
            volumeHud += "[white on white] [/]" if volume > self.volumeAtual else "[cyan1 on cyan1] [/]"
        return volumeHud

    def aumentar_volume(self) -> None:
        if self.ligado:
            self.volumeAtual += 1 if self.volumeAtual < ControleRemoto.volumeMax else 0
            
    def diminuir_volume(self) -> None:
        if self.ligado:
            self.volumeAtual -= 1 if self.volumeAtual > ControleRemoto.volumeMin else 0
    
    def avancar_canal(self) -> None:
        if self.ligado:
            self.canalAtual += 1 if self.canalAtual < ControleRemoto.canalMax else -(ControleRemoto.canalMax - 1)

    def retroceder_canal(self) -> None:
        if self.ligado:
            self.canalAtual -= 1 if self.canalAtual > ControleRemoto.canalMin else -(ControleRemoto.canalMax - 1)

    def ligar_desligar(self) -> None:
        self.ligado = True if self.ligado == False else False

    def botoes_controle(self, botao:str) -> None:
        match botao.strip()[0]:
            case "@":
                self.ligar_desligar()
            case "+":
                self.aumentar_volume()
            case "-":
                self.diminuir_volume()
            case ">":
                self.avancar_canal()
            case "<":
                self.retroceder_canal()
            case "0":
                quit()
            case _:
                pass

    def hud_tv(self) -> None:
        system("clear")
        status = ""
        if self.ligado == False:
            status = Panel.fit("[red]:prohibited: A TV está desligada[/]", title="[ TV ]")
        elif self.ligado == True:
            conteudo = f"CANAL = {self.hud_canais()}\n\n"
            conteudo += f"VOLUME = {self.hud_volumes()}"
            status = Panel.fit(conteudo, title="[ TV ]")
        print(status)
        self.botoes_controle(str(input(f"< CH{self.canalAtual} >\t - VOL{self.volumeAtual} + ")))
        self.hud_tv()


tv = ControleRemoto()
tv.hud_tv()
