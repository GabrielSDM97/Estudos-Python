from menuLib.formato import *
from menuLib.leiaNum import *
from time import sleep


def opção(opção, nomeArq):
    if opção <= len(opçõesfunc):
        return opçõesfunc[opção-1](nomeArq)
    print('\033[91mOpção inválida, tente novamente!\033[m')
    sleep(1)


def op1(nomeArq):
    cabeçalho('NOVO CADASTRO')
    while True:
        try:
            with open(nomeArq, 'at+') as arquivo:
                arquivo.write(f"{str(input('Nome: ')).strip()};{int(input('Idade: '))}\n")
                print(f'\nCadastro efetuado com sucesso!')
                sleep(1)
                break            
        except (KeyboardInterrupt, ValueError):
            print(f'\033[91mERRO! Por favor, tente novamente!\033[m')


def op2(nomeArq):
    cabeçalho('CADASTROS')
    try:
        with open(nomeArq, 'r') as arquivo:
            conteudoArquivo = arquivo.readlines()
            if len(conteudoArquivo) == 0:
                print("Não há nenhum cadastro a ser mostrado!")
                return sleep(1)
            for idLinha, conteudoLinha in enumerate(conteudoArquivo):
                dadosCadastro = conteudoLinha.split(';')
                print(f'ID:{idLinha} - {dadosCadastro[0]:<25}{dadosCadastro[1].strip('\n')} anos')
        sleep(1)
    except:
        print(f'\033[91mERRO ao tentar abrir o arquivo!\033[m')


def op3(nomeArq):
    cabeçalho('ATUALIZAR UM CADASTRO')
    while True:
        try:
            with open(nomeArq, 'r') as arquivo:
                conteudoArquivo = arquivo.readlines()
                if len(conteudoArquivo) == 0:
                    print("Não há nenhum cadastro a ser atualizado!")
                    return sleep(1)
                while True:
                    idCadastro = int(input("Deseja atualizar qual cadastro (ID)?"))
                    if idCadastro >= 0 and idCadastro < len(conteudoArquivo):
                        break
                    print("\033[91mID inválido, tente novamente!\033[m")
            with open(nomeArq, 'w') as arquivo:
                for idLinha, conteudoLinha in enumerate(conteudoArquivo):
                    if idCadastro == idLinha:
                        arquivo.write(f"{str(input("Digite o novo nome: ")).strip()};{int(input("Digite a nova idade: "))}\n")
                    elif idCadastro != idLinha:
                        arquivo.write(conteudoLinha)
                print(f"\nAtualização efetuada com sucesso!")
                sleep(1)
                break
        except (KeyboardInterrupt, ValueError, IndexError):
            print(f'\033[91mERRO! Por favor, tente novamente!\033[m')


def op4(nomeArq):
    cabeçalho('REMOVER UM CADASTRO')
    while True:
        try:
            with open(nomeArq, 'r') as arquivo:
                conteudoArquivo = arquivo.readlines()
                if len(conteudoArquivo) == 0:
                    print("Não há nenhum cadastro a ser removido!")
                    return sleep(1)
                while True:
                    idCadastro = int(input("Deseja remover qual cadastro (ID)? "))
                    if idCadastro >= 0 and idCadastro < len(conteudoArquivo): 
                        break
                    print("\033[91mID inválido, tente novamente!\033[m")
            with open(nomeArq, 'w') as arquivo:
                for idLinha, conteudoLinha in enumerate(conteudoArquivo):
                    if idLinha != idCadastro:
                        arquivo.write(conteudoLinha)
                print(f'\nCadastro removido com sucesso!')
                sleep(1)
                break
        except (KeyboardInterrupt, ValueError, IndexError):
            print("\033[91mERRO! Por favor, tente novamente!\033[m")


def op5(_):
    cabeçalho('SAINDO DO SISTEMA')
    print('Saindo do sistema', end='')
    for ponto in range(3):
        sleep(1)
        print('.', end='', flush=True)
    sleep(1)
    print('\nAté logo!')
    quit()

opçõesfunc = [op1, op2, op3, op4, op5]
