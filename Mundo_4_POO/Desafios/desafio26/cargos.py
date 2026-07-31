from funcionario import Funcionario
from rich.traceback import install
install()


class Horista(Funcionario):
    def __init__(self, nome, valor_hora, horas_trab):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

    def calc_sal(self):
        self.sal_bruto = self.valor_hora * self.horas_trab
        self.salario = self.sal_bruto - (self.sal_bruto * (Funcionario.inss/100))


class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto):
        super().__init__(nome, sal_bruto)

    def calc_sal(self):
        self.salario = self.sal_bruto - (self.sal_bruto * (Funcionario.inss/100))
