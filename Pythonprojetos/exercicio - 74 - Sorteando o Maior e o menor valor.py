from random import randint
print('Exercicio - 74 Crie um programa que vai gerar cinco '
      'números aleatórios e colocar em uma tupla. Depois disso, \n '
      'mostre a listagem de números gerados e também indique o \n'
      ' menor e o maior valor que estão na tupla.')

print('=+'*30)
print('Maior e menor valores em Tupla')
print('=+'*30)

n = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'Eu sorteei o valor {n}')
print(f'O maior valor sorteado foi {max(n)}')
print(f'O Menor valor sorteado foi {min(n)}')


