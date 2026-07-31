# Definindo funções para essa biblioteca as quais poderão ser importadas.

def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f

def dobro(n):
    d = n * 2 
    return d

def triplo(n):
    t = n * 3
    return t
