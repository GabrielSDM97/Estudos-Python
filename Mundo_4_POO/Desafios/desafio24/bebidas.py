from bebida_quente import BebidaQuente
from rich.traceback import install
install()


class Cafe(BebidaQuente):
    def servir(self):
        print("3. Servindo em xícara pequena.\n--- Bebida Pronta ---")

    def misturar(self):
        print("2. Passando água pressurizada pelo pó de café moído.")


class Cha(BebidaQuente):
    def servir(self):
        print("3. Servindo com canela na porcelana com limão.\n--- Bebida Pronta ---")

    def misturar(self):
        print("2. Mergulhando o sachê de ervas na água.")


class Leite(BebidaQuente):
    def servir(self):
        print("3. Servindo na caneca grande, já com café.\n--- Bebida Pronta ---")

    def misturar(self):
        print("2. Passando vapor pressurizado pelo bico do leite.")
