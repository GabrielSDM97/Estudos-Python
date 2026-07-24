from time import sleep

class NomeIdade():
    """
    Classe usada para mostrar nome, idade e forçar aniversário.
    variável = NomeIdade(nome, idade)
    """
    
    # Definindo parâmetros e argumentos padrão para os atributos do método construtor.
    def __init__(self, nome="vazio", idade=0):
        self.nome = nome
        self.idade = idade

        # É possível colocar estruturas e funções dentro do método construtor.
        print("Análisando", end = "")
        for c in range(3): 
            print(".", end = "", flush = True)
            sleep(0.5)
        
    def aniversario(self):
        self.idade += 1

    ''' String que representa o objeto quando este é chamado. 
    Sem este método, caso o objeto fosse chamado, mostraria o endereço na memória onde o objeto está. '''
    def __str__(self):  # Dunder method
        return f"{self.nome} tem {self.idade} anos!"

    # Customizando o retorno do dunder method "__getstate__"
    def __getstate__(self):  # Dunder method
        return f"Estado: nome = {self.nome}; idade = {self.idade}"


# Passando nome e idade pelos parâmetros da classe.
pessoa1 = NomeIdade("Maria", 28)
# Ao utilizar o nome do objeto, retorna o dunder method "__str__"
print(pessoa1)
pessoa1.aniversario()
print(pessoa1)

pessoa2 = NomeIdade("José", 34)
print(f"{pessoa2.nome} tem {pessoa2.idade} anos!")
pessoa2.aniversario()
print(pessoa2)

pessoa3 = NomeIdade()
print(f"{pessoa3.nome} tem {pessoa3.idade} anos!")
pessoa3.aniversario()
print(pessoa3)

# Mostra descrição/documentação/docstring da classe de um objeto.
print(pessoa1.__doc__)  # Dunder attribute

# Mostra classe de um objeto
print(pessoa1.__class__)  # Dunder attribute

# Mostra atributo como chave e estado como valor.
print(pessoa1.__dict__)  # Dunder attribute

# Por padrão, funciona que nem "__dict__", porém é customizável.
print(pessoa1.__getstate__())  # Dunder method
