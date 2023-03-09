print('Desafio 22 - Crie um programa que leia o nome completo de uma pessoa e mostre: '
      'O nome com todas as letras maiúsculas e minúsculas'
      'Quantas letras ao todo sem considerar espaços'
      'Quantas letras tem o primeiro nome.')

print('=*' * 30)
print('Analisador de Textos')
print('=*' * 30)

nome = str(input('Por favor digite o seu nome completo: ')).strip()
nome2 = nome.replace(' ','')
nome3 = nome.split()

print(f'Seu nome em letras maiusculas fica assim {nome.upper()}')
print(f'Seu nome em letras maiusculas fica assim {nome.lower()}')
print(f'Seu nome tem {len(nome2)} letras')
print(f'Seu primeiro nome tem {len(nome3[0])} letras')



