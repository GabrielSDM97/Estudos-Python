from os import system
from veiculos import *
from rich.table import Table
from rich.traceback import install
install()


def main():
    
    while True:
        system("clear")
        tabelaEntregas = Table(title="Tabela de entregas")
        dist = float(input("Distância: "))

        listaViagens = [Moto(dist), Caminhao(dist), Drone(dist)]
        
        tabelaEntregas.add_column("Distância", justify="left")
        tabelaEntregas.add_column("Tipo", justify="left")
        tabelaEntregas.add_column("Frete", justify="left")

        for viagem in listaViagens:
            tabelaEntregas.add_row(f"[yellow bold]{dist}KM[/]", f"[bold]{viagem.__class__.__name__}[/]", f"{viagem.calc_frete()}")
        print(tabelaEntregas)

        continuar = str(input("Deseja verificar uma nova distância? [S/N] "))
        if continuar in "Nn": break


if __name__ == "__main__":
    main()
