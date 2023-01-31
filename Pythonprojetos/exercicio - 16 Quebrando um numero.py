print ('Exercicio - 16 Crie um programa que lia um número Real qualquer pelo teclado e mostre na tela somente a parte inteira')
import math
A = float(input("Digite um número: "))
print('A parte inteira do numero {} é {}'.format(A, math.trunc(A)))