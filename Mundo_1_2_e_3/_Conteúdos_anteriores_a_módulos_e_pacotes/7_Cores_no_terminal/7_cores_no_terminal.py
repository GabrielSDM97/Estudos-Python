'''

O Python segue o padrão de coloração ANSCI (escape sequence), segue os códigos das cores abaixo:

# Style
Estilos: 

0 - None

1 - Bold

4 - Underline

7 - Negative (Inverte as cores)

# Text
Texto com cores normais:                Texto com Cores brilhantes:  

30 - Preto                              90 - Preto

31 - Vermelha                           91 - Vermelha

32 - Verde                              92 - Verde

33 - Amarela                            93 - Amarela

34 - Roxo                               94 - Roxo

35 - Magenta                            95 - Magenta

36 - Ciano                              96 - Ciano 

37 - Branca                             97 - Branca

# Back
Fundo com cores normais:                Fundo com Cores brilhantes: 

40 - Preto                              100 - Preto

41 - Vermelha                           101 - Vermelha

42 - Verde                              102 - Verde

43 - Amarela                            103 - Amarela

44 - Roxo                               104 - Roxo

45 - Magenta                            105 - Magenta

46 - Ciano                              106 - Ciano 

47 - Branca                             107 - Branca

'''

# A sintaxe padrão para colorir é \033[style;text;backm
# Obs.: O código de text e back podem vir em qualquer sequência, não necessariamente back depois de text já que são códigos diferentes.

# Exemplos

# Inserindo na própria string
print('\033[1;43;94mOlá, mundo!\033[m')

# Inserindo no ".format()"
print('Estou aprendendo a {}{}{}!!!'.format('\033[1;90;41m', 'colorir', '\033[m'))

########################
# Dicionário de cores: #
########################

cores = {'LIMPAR': '\033[m',
         'AMARELO': '\033[93m'}

print(f'Aprendi inclusive a criar um {cores['AMARELO']} dicionário de cores {cores['LIMPAR']}!!!')
