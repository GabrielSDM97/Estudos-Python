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


def resumo(preço = 0, porc_aum = 0, porc_red = 0, formatar = False):
    """
    Função para fazer cálculos de acrescimo, redução, dobro e metade de um dado preço, e formatá-lo.

    - preço = Valor a ser calculado.
    - porc_aum = Porcentagem de aumento sobre o parâmetro 'preço'
    - porc_red = Porcentagem de redução sobre o parâmetro 'preço'
    - formatar = Define se os resultados serão formatados desta forma: R$ 0,00.
    """
    from time import sleep
    c = 0
    print()
    while c <= 100:
        print(f'\rAnalisando o preço {moeda(preço)}: {c}%', end=' ', flush = True)
        c += 1
        sleep(0.05)
    print('\n')
    print(13*'~', 'RESUMO', '~'*13)
    print(f' Acrescentando {porc_aum}%: \t{aumentar(preço, porc_aum, formatar)}')
    print(f' Reduzindo {porc_red}%: \t{diminuir(preço, porc_red, formatar)}')
    print(f' Dobro de {moeda(preço)}: \t{dobro(preço, formatar)}')
    print(f' Metade de {moeda(preço)}: \t{metade(preço, formatar)}')
    print(34*'~')
