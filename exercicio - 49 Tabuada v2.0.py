print('Exercicio - 49 Refaça o exercicio 009 mostrando a tabuada de um numero que o usuario escolher só que \n'
      'agora utilizando o laço for')
from time import sleep
print('=-/*'*30)
print('\033[1:33m Tabuada versão 2.0 \033[m')
print('=-/*'*30)
n = int(input('Por gentileza digite um numero que mostraremos a tabuada até o 10: '))
for c in range(1,10+1):
    r = n * c
    sleep(1)
    print('{} * {} = {}'.format(n,c,r))