from rich import print
# A classe "Panel" desenha uma borda em volta do texto do primeiro argumento.
from rich.panel import Panel

# Instanciando o objeto "caixa" de acordo com a classe "Panel".
caixa = Panel(" Olá Mundo!", title="Bem-vindo", style="red", width=16)

print(caixa)
