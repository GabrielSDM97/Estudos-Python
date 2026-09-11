from superclasse import Pagamento
from rich import print
from rich.traceback import install
install()


class Boleto(Pagamento):
    def pagar(self, valor: float):
        self.valor = valor
        return f"Pagamento [green]CONFIRMADO[/] de [green]{self.fvalor}[/] via Boleto"


class PIX(Pagamento):
    def pagar(self, valor: float):
        self.valor = valor
        return f"Pagamento [green]CONFIRMADO[/] de [green]{self.fvalor}[/] via Pix"


class Credito(Pagamento):
    def pagar(self, valor: float):
        self.valor = valor
        return f"Pagamento [green]CONFIRMADO[/] de [green]{self.fvalor}[/] via Cartão de Crédito"


# Método polimórfico (Duck Typing)
def finalizar_compra(obj: object, valor: float):
    print(obj.pagar(abs(valor)))
