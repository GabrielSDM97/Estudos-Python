class ContaBancaria:
    def __init__(self, numero_conta: int, titular: str, saldo: float):
        # Tipos de visibilidade
        self.id: int = numero_conta  # Público (+)
        self._titular: str = titular  # Protegido (#)
        self.__saldo: float = saldo  # Privado (-)

    def __str__(self) -> str:
        return f"Estado atual da conta: {self.__dict__}"

    def sacar(self, valor: float) -> None:
        valor = abs(valor) # Valor absoluto (útil para tornar negativos em positivos)
        if valor > self.__saldo:
            print(f"\033[91mSaldo insuficiente!\033[m\n")
        else:
            self.__saldo -= valor
            print(f"Saque de R${valor:,.2f} efetuado com sucesso!\n")

    def depositar(self, valor: float) -> None:
        valor = abs(valor)
        self.__saldo += valor
        print(f"Depósito de \033[92mR${valor:,.2f}\033[m efetuado com sucesso!\n")
