from subclasses import *
from rich import print
from rich.traceback import install
install()

# Regras do sistema
# Utilizaremos um método polimórfico (duck type) para instanciar um objeto, o qual representa
# um tipo de pagamento, e enviar o valor da compra, que será atribuido a um método validável
# e depois formatado para REAIS.

def main():
    tipo_pag = [Boleto, Credito, PIX]
    pag_txt = "\nBoleto(0) | Crédito(1) | PIX(2): "
    val_txt = "Valor a ser pago: "

    while True:
        try:
            # É possível instanciar um objeto ao passar um chamamento de classe como argumento de uma função.
            finalizar_compra(tipo_pag[abs(int(input(pag_txt)))](), float(input(val_txt)))
        except ValueError:
            print(f"[red bold]Valor inválido, tente novamente![/]")
        except IndexError:
            print(f"[red bold]Opção inválida, tente novamente![/]")

        continuar = str(input("\nFazer novo pagamento? [S/N] "))
        if continuar in "Nn":
            break


if __name__ == "__main__":
    main()
