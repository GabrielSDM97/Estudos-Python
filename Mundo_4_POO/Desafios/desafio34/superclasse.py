from rich.panel import Panel
from rich.traceback import install
install()


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario

    def __str__(self):
        return f"O salário do {self.__class__.__name__} {self.nome} é de R${self.salario:,.2f}, e o bônus é de R${self.calcular_bonus():,.2f}"

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario):
        if salario < self.__salario:
            raise ValueError("Você não pode reduzir o salário de um funcionário!")
        self.__salario = salario

    def calcular_bonus(self):
        return self.salario * 0
