from rich import print
from poligonos import Circulo, Quadrado
from rich.traceback import install
install()


def main():
    poligono1 = Circulo(12)
    print(f"\n{poligono1}\n"
          f"Perímetro: {poligono1.perimetro():.1f} cm\n"
          f"Área: {poligono1.area():.1f} cm²\n")

    poligono2 = Quadrado(20)
    print(f"{poligono2}\n"
          f"Perímetro: {poligono2.perimetro():.1f} cm\n"
          f"Área: {poligono2.area():.1f} cm²\n")


if __name__ == "__main__":
    main()
