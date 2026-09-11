from abc import ABC, abstractmethod
from rich.traceback import install
from rich.panel import Panel
install()


class Funcionario(ABC):
    inss = 7.5
    sal_min = 1612.00

    def __init__(self, nome: str, sal_bruto: float = 0, salario: float = 0):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = salario

    def analisar_sal(self) -> "Panel":
        salarios_min = self.salario/Funcionario.sal_min
        mensagem = f"O salário de [yellow bold]{self.nome}[/] "
        mensagem += f"([dark_blue bold]{self.__class__.__name__}[/]) "
        mensagem += f"é de [green bold]R${self.salario:,.2f}[/] "
        mensagem += f"e corresponde a [rosy_brown bold]{(salarios_min):.1f}[/] salários mínimos."
        painel_sal = Panel(mensagem, title="Análise de Salário", width=50)
        return painel_sal

    @abstractmethod
    def calc_sal(self) -> None:
        pass
