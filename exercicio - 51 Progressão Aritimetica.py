print('Exercicio - 51 Desenvolva um programa que leia o primeiro termo  e a razao de uma PA, no final \n'
      'mostre os 10 primeiros termos dessa progressão')
print('#'*30)
print('\033[1:32m PROGRESSÃO ARITIMETICA \033[m')
print('#'*30)
soma = 0
pt = int(input('Digite o \033[1:31m Primeiro Termo:\033[m '))
r  = int(input('Digite a \033[1:31m razão \033[m que será usada: '))
for c in range (1,11):
    print('{} '.format(soma), end='')
    soma = soma + r + (pt)
print('ACABOU')