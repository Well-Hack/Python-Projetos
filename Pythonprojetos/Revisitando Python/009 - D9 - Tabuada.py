print('Desafio 9 - Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.')

print('=*'*30)
print('Tabuada')
print('=*'*30)

n1 = int(input('Digite um numero que diremos a tabuada dele até o 10: '))
c = 0
while(c <= 10):
    s = n1 * c
    print(f'{n1} x {c} = {s}')
    c += 1
print('fim')
