def aumentar(preço = 0, porcentagem = 0, formatar = False):
    """
    Função para aumentar um valor em uma dada porcentagem.

    - preço = Valor monetário.
    - porcentagem = Porcentagem de acréscimo para o parâmetro preço.
    - formatar = Define se o valor final será formatado desta forma: R$ 0,00.
    """
    r = preço + (preço * (porcentagem/100))
    return moeda(r) if formatar else r


def diminuir(preço = 0, porcentagem = 0, formatar = False):
    """
    Função para reduzir um valor em uma dada porcentagem.
    
    - preço = Valor monetário.
    - porcentagem = Porcentagem de redução para o parâmetro preço.
    - formatar = Define se o valor final será formatado desta forma: R$ 0,00.
    """
    r = preço - (preço * (porcentagem/100))
    return moeda(r) if formatar else r


def dobro(preço = 0, formatar = False):
    """
    Função para dobrar um dado preço.

    - preço = Valor a ser dobrado.
    - formatar = Define se o valor final será formatado desta forma: R$ 0,00.
    """
    r = preço * 2
    return moeda(r) if formatar else r


def metade(preço = 0, formatar = False):
    """
    Função para dividir pela metade um dado preço.

    - preço = Valor a ser dividido pela metade.
    - formatar = Define se o valor final será formatado desta forma: R$ 0,00.
    """
    r = preço/2
    return moeda(r) if formatar else r


def moeda(preço = 0, moeda = 'R$'):
    """
    Função para formatar um dado preço.

    - preço = Valor a ser formatado.
    - moeda = Padrão de moeda que aparecerá na posição prefixa ao valor final.
    """
    return f'{moeda}{preço:.2f}'.replace('.', ',')
