from rich import print
from poligonos import Circulo, Quadrado
from rich.traceback import install
install()


def main():
    poligono1 = Circulo(20)
    print(f"\n{poligono1}\n"
          f"Perímetro: {poligono1.perimetro():.1f}\n"
          f"Área: {poligono1.area():.1f}\n")

    poligono2 = Quadrado(12)
    print(f"{poligono2}\n"
          f"Perímetro: {poligono2.perimetro():.1f}\n"
          f"Área: {poligono2.area():.1f}\n")


if __name__ == "__main__":
    main()
