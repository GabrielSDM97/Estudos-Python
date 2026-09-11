from superclasse import Funcionario
from rich.traceback import install
install()


class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.15


class Designer(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.08


class Desenvolvedor(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.1
