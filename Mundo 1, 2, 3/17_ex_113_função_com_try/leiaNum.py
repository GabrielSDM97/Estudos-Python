def leiaInt(msg):
    print(5*'~'+'Número inteiro'+'~'*5, end='')
    while True:
        try:
            valorInt = int(input(f'{msg}\033[92m'))
        except KeyboardInterrupt:
            print('\n\n\033[91mO usuário decidiu não inserir um valor!')
            return 0
        except:
            print('\n\033[91mValor inválido. Insira um valor inteiro!\033[m')
        else:
            return f'{valorInt}'


def leiaFloat(msg):
    print('\033[m')
    print('\n'+5*'~'+'Número real'+'~'*5, end='')
    while True:
        try:
            valorFloat = float(input(f'{msg}\033[92m'))
        except KeyboardInterrupt:
            print('\n\n\033[91mO usuário decidiu não inserir um valor!')
            return 0
        except:
            print('\n\033[91mValor inválido. Insira um valor real!\033[m')
        else:
            return f'{valorFloat:.1f}'
