def cabeçalho(msg):
    print('\033[m'+20*'~~')
    print(f'{msg:^40}')
    print(20*'~~')


def hudMenuOpções():
    cabeçalho('Menu Principal')
    for pos, elemento in enumerate(opçõesdesc):
        print(f'\033[93m{pos+1} - \033[96m{elemento}')
    print('\033[m'+20*'~~')


opçõesdesc = ['Cadastrar nova pessoa', 'Ver pessoas cadastradas', 'Atualizar um cadastro', 'Remover um cadastro', 'Sair do sistema']
