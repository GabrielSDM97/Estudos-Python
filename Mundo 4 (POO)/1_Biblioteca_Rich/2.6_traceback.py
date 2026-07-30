from rich import print
from rich.traceback import install
install()  # Erros passam a ser monitorados pela biblioteca "rich"

print(50/0)
