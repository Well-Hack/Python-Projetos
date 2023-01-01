nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!\nTenha um bom dia {}'.format(nome))
elif nome == 'Carlos':
    print('O seu nome é estranho {}'.format(nome))
elif nome == 'João' or 'joao' or 'Joao':
    print('É do pé de feijão? kkkk')
else:
    print('Bom dia {}!'.format(nome))