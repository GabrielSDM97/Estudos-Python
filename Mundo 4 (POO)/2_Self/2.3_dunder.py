from time import sleep

class NomeIdade():
    """
    Classe usada para mostrar nome, idade e forçar aniversário.
    variável = NomeIdade(nome, idade)
    """
    
    # Definindo parâmetros e argumentos padrão para os atributos do método construtor.
    def __init__(self, nome:str="vazio", idade:int=0):
        self.nome:str = nome
        self.idade:int = idade

        # É possível colocar estruturas e funções dentro do método construtor.
        print("\nAnálisando", end = "")
        for c in range(3): 
            print(".", end = "", flush = True)
            sleep(0.5)
        
    def aniversario(self) -> None:
        self.idade += 1

    ''' String que representa o objeto quando este é chamado. 
    Sem este método, caso o objeto fosse chamado, mostraria o endereço na memória onde o objeto está. '''
    def __str__(self) -> str:  # Dunder method
        return f"\n{self.nome} tem {self.idade} anos!"

    # Customizando o retorno do dunder method "__getstate__"
    def __getstate__(self) -> str:  # Dunder method
        return f"Estado: nome = {self.nome}; idade = {self.idade}"


pessoa1 = NomeIdade("Maria", 28)
# Ao utilizar o nome do objeto, retorna o dunder method "__str__"
print(pessoa1)
pessoa1.aniversario()
print(pessoa1)

pessoa2 = NomeIdade("José", 34)
print(pessoa2)
pessoa2.aniversario()
print(pessoa2)

pessoa3 = NomeIdade()
print(pessoa3)
pessoa3.aniversario()
print(pessoa3)

# Mostra descrição/documentação/docstring da classe de um objeto.
print("\n1", pessoa1.__doc__)  # Dunder attribute

# Retorna o objeto da classe de origem do objeto instanciado.
print("\n2", pessoa1.__class__) # Dunder attribute

# Retorna o nome da classe do objeto formatado como string.
print("\n3", type(pessoa1).__name__, "ou", pessoa1.__class__.__name__) # Dunder attribute

# Mostra atributo como chave e estado como valor.
print("\n4", pessoa1.__dict__)  # Dunder attribute

# Por padrão, funciona que nem "__dict__", porém é customizável.
print("\n5", pessoa1.__getstate__())  # Dunder method
