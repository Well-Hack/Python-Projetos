print('Desafio 25 - Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.')

print('=*' * 30)
print('Procurando uma string dentro de outra')
print('=*' * 30)

nome = str(input('Digite seu nome completo, e diremos se tem SILVA em seu nome: ')).upper().strip()
nome2 = 'SILVA' in nome
print(f'seu nome tem silva? {nome2}')

