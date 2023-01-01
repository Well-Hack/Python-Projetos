print('Exercicio - 39 Faça um programa que leia o ano de nascimento de um jovem e informa de acordo com sua idade se ele: \n'
      ' * Se ele \033[1:32m ainda vai se alistar ao serviço militar \033[m \n'
      ' * Se \033[1:33m é a hora dele se alistar \033[m \n '
      ' * Se \033[1:34m já passou do tempo do alistamento \033[m \n'
      'Seu programa também deve mostrar o tempo que falta ou que passou do prazo')
nome = str(input('Bem vindo! Escreva seu nome por favor: '))
sex = int(input('Você é homem ou mulher? Digite [1] para homem ou [2] para mulher: '))
if sex == 2:
    print('Você não precisa se alistar no exercito.')
else:
    id = int(input('Agora digite a sua idade: '))
    if id < 18:
        id2 = 18 - id
        print('Você \033[1:34m não está na idade do alistamento militar,\033[m falta {} anos, para o seu alistamento'.format(id2))
    elif id == 18:
        print('Voce \033[1:32m está na idade de se alistar no Exercito. \033[m Por favor compareça a uma base mais proxima de você')
    else :
        id2 = id - 18
        print('Você \033[1:31m ESTÁ COM ATRASO  DE {} ANO(S) CON SUAS OBRIGAÇÕES MILITARES, \033[m Compareça \033[1:31m IMEDIATAMENTE \033[m  \n a'
            ' uma base mais proxima de sua residencia'.format(id2))