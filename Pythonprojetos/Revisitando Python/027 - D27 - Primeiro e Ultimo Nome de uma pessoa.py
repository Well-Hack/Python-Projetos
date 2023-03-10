print('Desafio 27 - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. ')
print('=*' * 30)
print('Primeiro e último nome de uma pessoa')
print('=*' * 30)


nome = str(input('Por favor digite o seu nome: ')).upper()
nome2 = nome.split()
nome3 = nome2[-1]
print(f'Seu nome completo é {nome} seu primeiro nome é {nome2[0]} e ultimo nome é {nome3}')
