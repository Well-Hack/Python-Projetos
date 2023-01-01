nome = str(input('|-----------|Concurso de Natação|----------| \n Bem Vindo! \n'
                 'Por gentileza, digite seu nome: '))
idade = int(input('Agora digite a sua idade: '))
print('LENDO OS DADOS, por favor aguarde...')
if idade <= 9:
    print('O participante {}, terá que participar na categoria: \033[1;32m MIRIM.\033[m'.format(nome))
elif idade > 9 and idade <= 14:
    print('O participante {}, terá que participar na categoria: \033[1;32m INFANTIL.\033[m'.format(nome))
elif idade > 14 and idade <= 19:
    print('O participante {}, terá que participar na categoria: \033[1;33m JÚNIOR.\033[m'.format(nome))
elif idade > 19 and idade <= 20:
    print('O participante {}, terá que participar na categoria: \033[1;33m SÊNIOR.\033[m'.format(nome))
elif idade > 20:
    print('O participante {}, terá que participar na categoria: \033[1;31m SÊNIOR.\033[m'.format(nome))
