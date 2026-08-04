from funcionario import Funcionario
from rich.traceback import install
install()


class Horista(Funcionario):
    def __init__(self, nome, valor_hora: float, horas_trab: int):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab
        self.sal_bruto = self.valor_hora * self.horas_trab

    def calc_sal(self):
        desconto = self.sal_bruto * (Funcionario.inss/100)
        self.salario = self.sal_bruto - desconto


class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto = Funcionario.sal_min):
        super().__init__(nome, sal_bruto)

    def calc_sal(self):
        desconto = self.sal_bruto * (Funcionario.inss/100)
        self.salario = self.sal_bruto - desconto