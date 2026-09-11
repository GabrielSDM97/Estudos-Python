from subclasses import *
from rich.traceback import install
install()

# Regras do sistema
# Simples algorítmo que simula o abrimento de arquivos, 
# mostrando nome, extensão, tamanho e programa "utilizado" para abrir tal arquivo.
# Obs.: O tamanho do arquivo definido no parâmetro da classe deve ser em Bytes.

# Neste sistema utilizamos um método Duck Type.

def main():
    arq1 = DOC("prova", 1_450_000)
    arq2 = PDF("estudos", 5_000_000)
    arq3 = PNG("cachorro", 250_000)

    abrir_arquivo(arq1)
    abrir_arquivo(arq2)
    abrir_arquivo(arq3)


if __name__ == "__main__":
    main()
