from subclasses import *
from rich import print
from rich.traceback import install
install()

# Regras do sistema
# 1. O bônus aplicado pelo método "calcular_bonus()" será diferente para cada subclasse:
# 1.1 Desenvolvedor: 10%
# 1.2 Designer: 8%
# 1.3 Gerente: 15%
# 2. Ao printar o objeto, mostra-se o salário e o bônus.
# 3. Ao printar o objeto chamando o método "calcular_bonus()"
# retorna-se o bônus sozinho.
# 4. Através do atributo "salario" é possível aumentar o salário
# porém não é possível diminuir.

# O polimorfismo aqui, trata-se do bônus salarial ser diferente em
# cada subclasse, apesar do método "calcular_bonus" ser o mesmo.

def main():
    func = Desenvolvedor("José", 1_500)
    print(func)
    print(func.calcular_bonus())

    func.salario = 1_600
    print(func)
    print(func.calcular_bonus())

    try:
        func.salario = 1_500
    except Exception as ex:
        print(f"[red bold]{ex.__class__.__name__}[/]: {ex}")


if __name__ == "__main__":
    main()
