from conta_bancaria import ContaBancaria
from rich import inspect, print
from rich.traceback import install
install()


def main():
    # Ao instanciar um objeto com a classe abaixo,
    # a criação da senha da conta faz-se necessária para cadastro da mesma,
    # seja como argumento pelo parâmetro "chave" ou pelo input do método "pede_senha".
    # A senha deve ter, no mínimo, 6 dígitos.
    conta1 = ContaBancaria(000, "José", 5_000.75, "")
    inspect(conta1, private=True, methods=True)

    # O algorítmo de saque verifica:
    # 1. Valores negativos, tornando-os positivos.
    # 2. Senha inválida, bloqueando o saque.
    # 3. Valor de saque acima do saldo, impedindo o saque.
    while True:
        try:
            # O método "sacar" pede a senha da conta caso não tenha sido definida na instanciação.
            print(conta1.sacar(float(input("Valor a ser sacado: "))))
        except Exception as ex:
            print(f"[red bold]{ex.__class__.__name__}:[/] {ex}")

        print(conta1)

        print(conta1.depositar(float(input("Valor a ser depositado: "))))

        print(conta1)

        continuar = str(input("Fazer novas transações? [S/N] "))
        if continuar in "Nn":
            break

    # Será requisitada a senha da conta para alterar o nome do titular.
    conta1.nome = str(input("Insira o novo nome do titular: "))
    inspect(conta1, private=True, methods=True)


if __name__ == "__main__":
    main()
