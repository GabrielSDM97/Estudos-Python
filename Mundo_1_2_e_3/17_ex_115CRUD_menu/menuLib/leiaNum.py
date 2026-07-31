def leiaInt(txt):
    while True:
        try:
            valorInt = int(input(f'\033[32m{txt}\033[92m'))
        except (KeyboardInterrupt, ValueError):
            print('\033[91mERRO: por favor, insira um número inteiro válido!\033[m')
        else:
            return valorInt
