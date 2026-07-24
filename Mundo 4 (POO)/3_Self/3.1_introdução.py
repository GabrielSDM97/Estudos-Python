
# === Evolução ===

# 1. Variáveis simples: Problema: Não era possível guardar múltiplos valores

# 2. Variáveis compostas (vetores/matrizes): Problema: Apresenta índices numéricos em vez de nomes

# 3. Dicionários: Problema: Separação entre dados e funções, assim como é também em variáveis simples e compostas.

# Variáveis simples, compostas e dicionários apenas armazenam dados. Para que tais estruturas sejam utilizadas
# em alguma funcionalidade no código, pra isso utilizamos funções a parte. 

# 4. Objetos: Paradigma atual: Além de armazenar dados, também executam funcionalidades com esses dados.


# "__" = Dunder (double underline)

# Declaração da classe (Convenção: Deve começar com letra maiúscula)
# "self" é substituido pelo nome do objeto

class MinhaClasse:
    # Atributo de classe - Todo objeto terá o mesmo estado deste atributo.
    especie = "Humano"

    # Método construtor
    def __init__(self):  # Dunder attribute

        # Atributos de instância - Cada objeto poderá ter estados diferentes destes atributos.
        self.nome = " "
        self.idade = 0

    # Métodos de instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self) -> str: # "-> tipo" serve como etiqueta mostrando o tipo de conteúdo que esse método deve retornar.
        return f"O {MinhaClasse.especie} {self.nome} tem {self.idade} anos!"
        #         self.__class__.especie

    def metodo_teste():
        # Quando é executado, nada acontece, porém evita erros em estruturas que não podem ficar vazias.
        pass # "pass" é usado como placeholder para códigos futuros.


# Para alterar um atributo de classe, é necessário chamá-lo através do nome da classe em si, não de um objeto,
# ou seja, tal atributo pode ser alterado antes mesmo da declaração de um objeto, já que dependende apenas da classe,
# e as mudanças feitas neste tipo de atributo afeta todo objeto instanciado depois dessa alteração.
MinhaClasse.especie = "Alien"

# Declaração de objeto
pessoa1 = MinhaClasse()  # Classe() => Chamada de instanciação => Método construtor
# objeto.atributo
pessoa1.nome = "Roberto"
pessoa1.idade = 28
# objeto.método()
print(pessoa1.mensagem())
pessoa1.aniversario()
print(pessoa1.mensagem())

pessoa2 = MinhaClasse()
pessoa2.nome = "José"
pessoa2.idade = 34
print(pessoa2.mensagem())
pessoa2.aniversario()
print(pessoa2.mensagem())

# A forma como atribuimos os estados acima foge às boas normas, na aula "3_ex2.py" faremos da forma correta.
