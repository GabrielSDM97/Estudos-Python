def leiaDinheiro(msg):
    """
    Função que verifica se um valor é monetário ou não.

    Retorna o valor em float.
    """
    while True:
        entrada = str(input(msg).strip().replace(',','.'))
        if entrada.replace('.','').isnumeric() and entrada.count('.') <= 1:
            return float(entrada)
        print(f'\033[91m"{entrada}" não é um valor monetário.\033[m')
