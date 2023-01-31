print('Exercicio 59 - Crie um programa que leia dois valores e mostre um menu na tela:'
      '1 - somar'
      '2 - Multiplicar'
      '3 - Maior '
      '4 - Novos numeros'
      '5 - sair do programa Seu programa deverá devera realizar a operação solicitada em cada caso.')
m = 0
print('#'*40)
print('Analisar de valores')
print('#'*40)
print('BEM VINDO!')
v1 = int(input('por gentileza, digite o primeiro valor: '))
v2 = int(input('Agora digite o segundo valor: '))
while m != 5:
    m = int(input('Agora selecione uma das opções abaixo: \n \033[031:1m [1] SOMAR \033[m \n \033[032:1m [2] MULTIPLICAR \033[m \n'
        '\033[033:1m  [3] MAIOR \033[m \n \033[034:1m [4] NOVOS NUMEROS \033[m \n \033[035:1m [5] SAIR DO PROGRAMA \033[m: '))
    if m == 1:
        r = v1 + v2
        print('O resultado da SOMA entre \033[031:1m {} \033[m e o \033[031:1m {} \033[m é de \033[032:1m {} \033[m'.format(v1,v2,r))
    if m == 2:
        r = v1 * v2
        print('O resultado da MULTIPLICAÇÃO entre \033[031:1m {} \033[m e o \033[031:1m {} \033[m é de \033[032:1m {} \033[m'.format(v1, v2, r))
    if m == 3:
            if v1 > v2:
                print('O \033[031:1m {} \033[m é MAIOR'.format(v1))
            elif v2 > v1:
                print('O \033[031:1m {} \033[m é MAIOR'.format(v2))
            else:
                print('Os dois numeros são iguais')
    if m == 4:
        v1 = int(input('por gentileza, digite o primeiro valor: '))
        v2 = int(input('Agora digite o segundo valor: '))
    else:
        print('Opção invalida, tente novamente ')
print('Obrigado, tenha um otimo dia!')


