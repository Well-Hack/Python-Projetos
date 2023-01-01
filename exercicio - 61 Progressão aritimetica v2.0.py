print('Exercicio - 61 Refaça o DESAFIO 51. Lendo o primeiro termo e a razão de uma PA. MOstrando os 10 primeiros '
      'termos da progressão usando a estrutura while. ')
print('#'*30)
print('\033[1:32m PROGRESSÃO ARITIMETICA VERSÃO 2.0\033[m')
print('#'*30)
soma = 0
soma2 = 0
pt = int(input('Digite o \033[1:31m Primeiro Termo:\033[m '))
r  = int(input('Digite a \033[1:31m razão \033[m que será usada: '))
while soma != 10:
    soma += 1
    print('{} '.format(pt), end='')
    pt += r
print('Acabou')