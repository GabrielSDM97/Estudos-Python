from conta_bancaria import ContaBancaria

def main():
    # O underscore "_" em "5_000" permite separar grupos de dígitos.
    # Serve apenas para facilitar a leitura visual de números grandes.
    conta1 = ContaBancaria(2845, "José", 5_000.75) 

    print(conta1.__doc__)

    conta1.saque(500.75)
    conta1.deposito(100.25)
    
    print(conta1)

    conta1.saque(-500.75)
    conta1.deposito(-100.25)

    print(conta1)

if __name__ == "__main__":
    main()
