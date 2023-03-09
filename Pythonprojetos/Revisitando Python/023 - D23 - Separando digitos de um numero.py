print('Desafio 23 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.')

print('=*' * 30)
print('Separando digitos de um numero')
print('=*' * 30)

n = int(input('Por gentileza, digite um número que contehha no maximo 4 digitos: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
um = n // 1000 % 10
print('Unidade:{}'.format(u))
print('Dezena: {}'.format(d))
print('Centena:{}'.format(c))
print('Milhar: {}'.format(um))