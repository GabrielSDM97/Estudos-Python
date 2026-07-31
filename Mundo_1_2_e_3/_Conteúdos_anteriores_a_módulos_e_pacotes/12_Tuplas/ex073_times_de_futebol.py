''' Exercício 73 - Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time do São Paulo. '''

times_brasileirao = (
    "Botafogo",
    "Palmeiras",
    "Fortaleza",
    "Flamengo",
    "São Paulo",
    "Bahia",
    "Cruzeiro",
    "Atlético-MG",
    "Vasco",
    "Internacional",
    "Grêmio",
    "Athletico-PR",
    "Criciúma",
    "Bragantino",
    "Juventude",
    "Fluminense",
    "Vitória",
    "Corinthians",
    "Cuiabá",
    "Atlético-GO"
)

print(f'a) Os 5 primeiros times:\n{times_brasileirao[:5]}')

print(f'\nb) Os últimos 4 colocados são:\n{times_brasileirao[-4:]}')

print(f'\nc) Times em ordem alfabética:\n{sorted(times_brasileirao)}') # Não altera a tupla, apenas organiza em ordem alfabética quando aparece no terminal.

print(f'\nd) Em que posição está o time de São Paulo:\nSão Paulo está na {times_brasileirao.index("São Paulo")+1}ª posição!')
