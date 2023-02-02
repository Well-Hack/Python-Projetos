print('Exercicio 013 - Crie um programa que leia o nome completamente de uma pessoa e mostre \n '
      '1* O nome com todas as letras maiuculas; \n '
      '2* O nome com todas minusculas; \n 3* Quantas letras ao todo, sem espaço; \n 4* Quantas letras tem o primeiro nome.')


nome = input('Olá, digite o seu nome completo que iremos analisa-lo por favor:').strip()
print('Seu nome em letras maiusculas fica {}'.format(nome.upper()))
print('Seu nome em letras minusculas fica {}'.format(nome.lower()))
nome2 = nome.replace(' ','')
nome3 = len(nome2)
separa = nome.split()
print('O seu nome completo sem espaço tem {} letras'.format(nome3))
print('O seu primeiro nome {} ele tem {} letras '.format(separa[0], len(separa[0])))

