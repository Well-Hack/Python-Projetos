print('Exercicio - 52 Faça um programa que leia um numero e diga se ele é ou não um número primo.')
num = int(input('Digite um numero: '))
tot = 0
for c in range(1,num + 1):
    if num % c == 0:
        tot += 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print('{}'.format(c),end=' ')
print('\nO numero {} foi divisivel por {} vezes'.format(num,tot))
if tot == 2:
    print('Por isso ele é PRIMO')
else:
    print('Ele não é PRIMO')