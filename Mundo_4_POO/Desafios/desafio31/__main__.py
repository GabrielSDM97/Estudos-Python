from retangulo import Retangulo
from rich import inspect, print
from rich.traceback import install
install()


# Regras do sistema
# 1. O sistema apenas aceita valores números positivos inteiros ou float
# 2. Podemos inserir o tamanho do retângulo de 3 formas:
# 2.1 Na instanciação: Retangulo(base, altura)
# 2.2 Com os atributos validáveis self.base = base e self.altura = altura
# 2.3 Com o atributo validável com tupla: self.medidas(base, altura)
# Não é possível inserir um valor de área diretamente.

def main():
    ret = Retangulo(10, 20)
    print(ret.medidas)

    try:
        ret.base = 30
        ret.altura = 40
        print(ret.medidas)
        ret.medidas = (50, 60)
    except Exception as ex:
        print(f"\n[red bold]{ex.__class__.__name__}[/]: {ex}")

    print(ret.medidas)

    # Vai gerar um erro, já que não é permitido inserir valores
    # diretamente na área.
    try:
        ret.area = 10
    except Exception as ex:
        print(f"\n[red bold]{ex.__class__.__name__}[/]: {ex}")

    inspect(ret, private=True, methods=True)


if __name__ == "__main__":
    main()
