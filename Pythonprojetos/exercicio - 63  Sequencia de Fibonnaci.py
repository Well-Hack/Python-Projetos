print('Exercicio - 63 Escreva um programa que leia um numero inteiro qualquer e mostre na tela os n \n primeiros'
      'elementos de uma sequencia de fibonacci ')
soma = 0
soma2 = 1
soma3 = 1
t = int(input('Quantos termos voce quer mostrar? '))
print('{} {} {}'.format(soma,soma2,soma3),end=' ')
while t - 3 != 0:
   soma = soma2 + soma3
   print('{} '.format(soma), end='')
   soma2 = soma3
   soma3 = soma
   t -= 1
print('Acabou!')