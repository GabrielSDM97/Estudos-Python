from abc import ABC, abstractmethod
from rich.traceback import install
from rich.panel import Panel
install()


class Funcionario(ABC):
    inss = 7.5
    sal_min = 1612

    def __init__(self, nome, sal_bruto=0, salario=0):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = salario

    def analisar_sal(self):
        painelSal = Panel(f"O salário de [yellow bold]{self.nome}[/] ([dark_blue bold]{self.__class__.__name__}[/]) é de [green bold]R${self.salario:,.2f}[/] "
                          f"e corresponde a [rosy_brown bold]{(self.salario/Funcionario.sal_min):.1f}[/] salários mínimos.", title="Análise de Salário", width=50)
        return painelSal

    @abstractmethod
    def calc_sal(self):
        pass
