from veiculos import *
from rich.traceback import install
from rich.table import Table
install()


def main():
    tabelaEntregas = Table(title="Tabela de entregas")
    dist = 100

    entrega1 = Moto(dist)

    entrega2 = Caminhao(dist)

    entrega3 = Drone(dist)

    tabelaEntregas.add_column("Distância", justify="left")
    tabelaEntregas.add_column("Tipo", justify="left")
    tabelaEntregas.add_column("Frete", justify="left")
    tabelaEntregas.add_row(f"{entrega1}", f"{entrega1.__class__.__name__}", f"{entrega1.calc_frete()}")
    tabelaEntregas.add_row(f"{entrega2}", f"{entrega2.__class__.__name__}", f"{entrega2.calc_frete()}")
    tabelaEntregas.add_row(f"{entrega3}", f"{entrega3.__class__.__name__}", f"{entrega3.calc_frete()}")
    
    print(tabelaEntregas)


if __name__ == "__main__":
    main()
