''' Exercício 105 - Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

    Quantidade de notas
    A maior nota
    A menor nota
    A média da turma
    A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor. '''


def notas(*notas, situação=False):
    """
    Demonstração:
    var = notas(5, 8.5, 10, situação=True)

    No parâmetro '*notas' podem ser inseridas quantas notas você quiser.
    O parâmetro 'situação=False ou True' mostra se a turma foi bem ou não. Este parâmetro é opcional.
    A função retorna um dicionário com o total de notas, maior nota, menor nota, media e situação da turma.
    """
    dicionário = dict()
    dicionário['Total de notas'] = len(notas)
    dicionário['Maior nota'] = max(notas)
    dicionário['Menor nota'] = min(notas)
    dicionário['Média da turma'] = f'{sum(notas)/len(notas):.1f}'
    if situação:
        if sum(notas)/len(notas) >= 7:
            dicionário['Situação'] = 'BOA'
        elif sum(notas)/len(notas) >= 5:
            dicionário['Situação'] = 'RAZOÁVEL'
        else:
            dicionário['Situação'] = 'RUIM'
    return dicionário


consulta = notas(6, 10, 8, situação=True)
print(consulta)
help(notas)
