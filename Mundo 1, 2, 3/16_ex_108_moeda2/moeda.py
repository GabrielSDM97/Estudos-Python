def aumentar(preço = 0, porcentagem = 0):
    r = preço + (preço * (porcentagem/100))
    return r


def diminuir(preço = 0, porcentagem = 0):
    r = preço - (preço * (porcentagem/100))
    return r


def dobro(preço = 0):
    r = preço * 2
    return r


def metade(preço = 0):
    r = preço/2
    return r


def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
