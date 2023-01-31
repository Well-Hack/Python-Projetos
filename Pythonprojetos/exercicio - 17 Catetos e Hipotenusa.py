import math
print ("Exercicio - 17 Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente "
       "de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.")
co = float(input('Comprimento do Cateto Oposto '))
ca = float(input('Comprimento do catento Adjacente '))
hi = math.hypot(ca,co)
print('A hipotenusa vai medir {:.2f}'.format(hi))