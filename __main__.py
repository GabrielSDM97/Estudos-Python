from hashlib import sha256
from rich import inspect, print
from rich.traceback import install
install()


class ContaBancaria:
    def __init__(self, id: int, titular: str, saldo: float, chave: str = None):
        self._id = id
        self._titular = titular
        self.__saldo = saldo
        self.__hash = sha256(chave.encode()).hexdigest() if chave else sha256(self.pede_senha().encode()).hexdigest()
        print(f"Conta {self._id} criada com sucesso! Saldo atual de [green bold]R${self.__saldo:,.2f}[/]")

    def __str__(self):
        return f"Saldo atual da conta {self._id}: R${self.__saldo:,.2f}"

    def validar_senha(self, chave: str) -> bool:
        hashChave = sha256(chave.encode()).hexdigest()
        return bool(hashChave == self.__hash)

    def pede_senha(self) -> str:
        from pwinput import pwinput
        while True:
            chave = str(pwinput("Senha: ", mask = "*")).strip()
            if len(chave) >= 6:
                break
            print("[red bold]Erro![/] A senha deve ter pelo menos 6 dígitos, tente novamente!")
        return chave

    def sacar(self, valor: float, chave: str = None) -> str:
        if valor > self.__saldo:
            raise ValueError("Saldo insuficiente!\n")    
        chave = self.pede_senha() if chave == None else chave
        if self.validar_senha(chave):
            valor = abs(valor)
            self.__saldo -= valor
            return f"Saque de [green bold]R${valor:,.2f}[/] efetuado com sucesso!\n"
        raise PermissionError("Senha inválida! Saque não autorizado!\n")

    def depositar(self, valor: float) -> str:
        valor = abs(valor)
        self.__saldo += valor
        return f"Depósito de [green bold]R${valor:,.2f}[/] efetuado com sucesso!\n"

    @property
    def nome(self) -> str:
        return self._titular

    @nome.setter
    def nome(self, nome: str):
        if self.validar_senha(self.pede_senha()) == False:
            raise PermissionError("Senha inválida! Troca de titular não autorizada!\n")
        self._titular = nome


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
