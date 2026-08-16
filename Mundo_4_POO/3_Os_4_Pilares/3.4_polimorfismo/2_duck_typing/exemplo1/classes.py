from rich.traceback import install
install()


class Porta:
    def abrir(self):
        print(f"Girar a maçaneta e empurrar/puxar a porta!\n")

class Empresa:
    def abrir(self):
        print(f"Vá até ao portal do empreendedor com toda a documentação para abrir um CNPJ!\n")

class Ovo:
    def abrir(self):
        print(f"Quebre a casca do ovo para abri-lo!\n")

class Pedra:
    pass

# Método Pythônico Polimórfico (Duck-Typing)
def tentar_abrir(objeto):
    try:
        objeto.abrir()
    except:
        print(f"Encontrei problemas ao tentar abrir {objeto.__class__.__name__}!\n")
