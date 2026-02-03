from menuLib.formato import *
from menuLib.leiaNum import *
from time import sleep


def opção(opção, nomeArq):
    if opção <= len(opçõesfunc):
        return opçõesfunc[opção-1](nomeArq)
    print('\033[91mOpção inválida, tente novamente!\033[m')
    sleep(1)


def op1(nomeArq):
    cabeçalho('CADASTROS')
    try:
        arquivo = open(nomeArq, 'rt')
        for linha in arquivo:
            dados = linha.split(';')
            print(f'{dados[0]:<30}{dados[1].strip('\n')} anos')
        sleep(1)
        arquivo.close()        
    except:
        print(f'\033[91mERRO ao tentar abrir o arquivo!\033[m')


def op2(nomeArq):
    cabeçalho('NOVO CADASTRO')
    while True:
        try:
            registro = [str(input('Nome: ').strip()), int(input('Idade: '))]
            with open(nomeArq, 'at+') as arquivo:
                arquivo.write(f'{registro[0]};{registro[1]}\n')
                print(f'\n{registro[0]} cadastrado/a com sucesso!')
                sleep(1)
                break            
        except (KeyboardInterrupt, ValueError):
            print(f'\033[91mERRO! Por favor, tente novamente!\033[m')


def op3(_):
    cabeçalho('SAINDO DO SISTEMA')
    print('Saindo do sistema', end='')
    for ponto in range(3):
        sleep(1)
        print('.', end='', flush=True)
    sleep(1)
    print('\nAté logo!')
    quit()


opçõesfunc = [op1, op2, op3]
