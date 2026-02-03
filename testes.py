'''while True:
    try:
        teste = str(input('Continuar? '))
    except Exception as erro:
        print(f'Erro: {erro}')
    else:
        break
    finally:
        print('Teste ABCDE')
print('ABC')'''


teste = 'abc dbc; abc'

print(teste.split(';'))
