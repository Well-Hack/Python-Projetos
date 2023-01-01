import string
nome = (str(input('Por favor. Escreva seu nome COMPLETO: ')))
separa = nome.split()
print('Analisando os dados, por favor aguarde....')
print('O seu nome tem {} letras'.format((len(nome.replace(' ', '')))))
print('O seu nome em letras maiusculas fica {}'.format(nome.upper()))
print('O seu nome em letras maiusculas fica {}'.format(nome.lower()))
print('O seu primeiro nome {}  ele tem {} letras '.format(separa[0], len(separa[0])))
