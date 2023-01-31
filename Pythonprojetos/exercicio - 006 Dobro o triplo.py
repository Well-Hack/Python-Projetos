print("006 - crie um algoritmo que leia um numero, e mostre o seu dobro, o seu triplo e a sua raiz")
n1 = int(input('Digite um número: '))
d1 = n1*2
t1 = n1*3
r1 = n1**(1/2)
print('O valor que você digitou foi {}, o seu dobro é {}, o seu triplo é {} e a sua raiz seria {:.2f}'.format(n1,d1,t1,r1))