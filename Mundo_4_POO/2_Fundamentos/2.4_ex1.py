# Crie uma classe com os atributos e métodos abaixo:

# Atributos:
# + Número da conta
# + Nome do titular
# + Saldo

# Métodos:
# + Depósitos
# + Saques

class ContaBancaria:
    """
    Cria um conta bancária, permitindo saques e depósitos!
    variavel = ContaBancaria(número da conta, nome do títular, saldo em reais)

    Métodos:
    variavel.saque(valor do saque)
    variavel.deposito(valor do deposito)

    Importante: O valor de saque deve ser igual ou menor que o saldo da conta.\n
    """

    def __init__(self, numero_conta:int, titular:str, saldo:float):
        self.id:int = numero_conta
        self.titular:str = titular
        self.saldo:float = saldo

    def __str__(self) -> str:
        return f"Número da conta: {self.id}\nTitular: {self.titular}\nSaldo atual: R${self.saldo:,.2f}!\n"

    def saque(self, valor:float) -> None:
        if valor > self.saldo:
            print(f"\033[91mSaldo insuficiente!\033[m\n")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} efetuado com sucesso!\n")

    def deposito(self, valor:float) -> None:
        self.saldo += valor
        print(f"Depósito de \033[92mR${valor:,.2f}\033[m efetuado com sucesso!\n")


conta1 = ContaBancaria(2845, "José", 999.75)
print(conta1.__doc__)

conta1.saque(2000.75)

conta1.deposito(100.25)

print(conta1)
