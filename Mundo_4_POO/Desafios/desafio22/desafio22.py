# Desafio 22

# Crie a classe ControleRemoto, onde vamos simular o funcionamento de um controle
# simples (canal, volume, e liga/desliga)

from os import system
from rich import print
from rich.traceback import install
from rich.panel import Panel
install()


class ControleRemoto:
    canal_min:int = 1
    volume_min:int = 1
    canal_max:int = 5
    volume_max:int = 5
 

    def __init__(self):
        self.ligado:bool = False
        self.volume_atual:int = 1
        self.canal_atual:int = 1

    def hud_canais(self) -> str:
        canais_hud = ""
        for canal in range(ControleRemoto.canal_min, ControleRemoto.canal_max+1):
            canais_hud += f" {canal} " if self.canal_atual != canal else f"[grey0 on green1] {canal} [/]"
        return canais_hud

    def hud_volumes(self) -> str:
        volume_hud = ""
        for volume in range(ControleRemoto.volume_min, ControleRemoto.volume_max+1):
            volume_hud += "[cyan1 on cyan1] [/]" if volume <= self.volume_atual else "[white on white] [/]"
        return volume_hud

    def aumentar_volume(self) -> None:
        if self.ligado:
            self.volume_atual += 1 if self.volume_atual < ControleRemoto.volume_max else 0
            
    def diminuir_volume(self) -> None:
        if self.ligado:
            self.volume_atual -= 1 if self.volume_atual > ControleRemoto.volume_min else 0
    
    def avancar_canal(self) -> None:
        if self.ligado:
            self.canal_atual += 1 if self.canal_atual < ControleRemoto.canal_max else -(ControleRemoto.canal_max - 1)

    def retroceder_canal(self) -> None:
        if self.ligado:
            self.canal_atual -= 1 if self.canal_atual > ControleRemoto.canal_min else -(ControleRemoto.canal_max - 1)

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
        self.botoes_controle(str(input(f"< CH{self.canal_atual} >\t - VOL{self.volume_atual} + ")))
        self.hud_tv()


tv = ControleRemoto()
tv.hud_tv()
