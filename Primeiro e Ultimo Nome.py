nome = str(input('Informa seu nome completo: ')).strip()
nomes = nome.split()
print('Seu primeiro nome é {}'.format(nomes[0]))
print('Seu ultimo nome é {}'.format(nomes[len(nomes)-1]))