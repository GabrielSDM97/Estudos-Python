# Type Hinting: anotações de tipo para documentação e análise estática.
# Não apresentam nenhuma funcionalidade, apenas servem para documentar o retorno esperado de uma função 
# ou conteúdo esperado em uma variável/parâmetro.
#
# Exemplos:
# Variável = "variavel:tipo = 10"
# Função/método e parâmetro = "def (parametro:tipo) -> tipo/None:" Usa-se None para funções que não retornam conteúdo.

class MinhaClasse:
    especie: str = "Humano"

    def __init__(self, nome: str, idade: int):  
        self.nome: str = nome 
        self.idade: int = idade

    def aniversario(self) -> None:
        self.idade += 1

    def mensagem(self) -> str:
        return f"O {self.__class__.especie} {self.nome} tem {self.idade} anos!"

    def metodo_teste():
        # "pass": instrução nula usada como placeholder em blocos que não podem ficar vazios.
        pass  # Placeholder: evita SyntaxError em um bloco vazio. Não executa nenhuma ação.


MinhaClasse.especie = "Alien"

# Passando nome e idade pelos parâmetros do método construtor da classe.
pessoa1 = MinhaClasse("Roberto", 28)
print(pessoa1.mensagem())
pessoa1.aniversario()
print(pessoa1.mensagem())

pessoa2 = MinhaClasse("José", 34)
print(pessoa2.mensagem())
pessoa2.aniversario()
print(pessoa2.mensagem())