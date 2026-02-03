''' Exercício 102 - Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial. '''

def fatorial(num, show=False):
    """
    -> Calcula fatorial de um número.
    -- Parâmetros --
    num : número que sera calculado.
    show=False : Mostra ou não o processo do cálculo na tela. True = Aparece o cálculo e resultado, False = Apenas o resultado.
    """
    resultado = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c} x' if c > 1 else f'{c} =', end=' ')
        resultado *= c
    return resultado


# Programa Principal
print(24*'==')
print(fatorial(10, show=True))
help(fatorial)
