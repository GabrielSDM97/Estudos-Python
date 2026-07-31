# Disponibiliza a função print com muito mais customizações, sobrepondo o print padrão do python.
from rich import print

# É possível colorir utilizando a linguagem markup BBCode, muito utilizada em foruns e na Steam, exemplo: "[cor]Texto[/]"
# Podemos utilizar emojis também, exemplo: ":emoji:"
print("Olá [red]mundo[/]! :earth_americas:")

# Comando de terminal para mostrar lista de emojis: "python3 -m rich.emoji"
# Cores: https://rich.readthedocs.io/en/stable/appendix/colors.html#appendix-colors
