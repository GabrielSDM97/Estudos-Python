from rich.traceback import install
# Documentação ABC (Abstract Base Classe): https://docs.python.org/3/library/abc.html
from abc import ABC, abstractmethod # Importando a classe ajudante "ABC" e o decorador "@abstractmethod"
install()

# Classe abstrata
class Pessoa(ABC): # => A classe ajudante "ABC" disponibiliza a infraestrutra para a criação de classes abstratas
    def __init__(self, nome:str = "", idade:int = 0):
        self.nome = nome
        self.idade = idade
    def fazer_aniversario(self, idade:int=0): # Método concreto
        self.idade += 1
    @abstractmethod # Decorador que obriga as subclasses a criarem o método abstrato abaixo
    def estudar(self):
        pass
