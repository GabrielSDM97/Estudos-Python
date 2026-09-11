from os import system
from veiculos import *
from rich.table import Table
from rich.traceback import install
install()


def main():
    
    while True:
        system("clear")
        tabela_entregas = Table(title="Tabela de entregas")
        dist = float(input("Distância: "))

        lista_viagens = [Moto(dist), Caminhao(dist), Drone(dist)]
        
        tabela_entregas.add_column("Distância", justify="left")
        tabela_entregas.add_column("Tipo", justify="left")
        tabela_entregas.add_column("Frete", justify="left")

        for viagem in lista_viagens:
            tabela_entregas.add_row(f"[yellow bold]{dist}KM[/]", f"[bold]{viagem.__class__.__name__}[/]", f"{viagem.calc_frete()}")
        print(tabela_entregas)

        continuar = str(input("Deseja verificar uma nova distância? [S/N] "))
        if continuar in "Nn": break


if __name__ == "__main__":
    main()
