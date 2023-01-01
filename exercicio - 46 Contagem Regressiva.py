print('Exercicio - 46 Faça um programa que mostre na tela uma contagem de regressiva par ao estouro de fogos de artificio \n'
      'indo de 10 até 0 com tempo de espera de 1 segundo entre eles')
print('=-'*30)
print('\033[1:33m FESTA DE FIM DE ANO \033[m')
print('-='*30)
from time import sleep
n = str(input('Por gentileza, digite \033[1:34m SIM \033[m para começar a contagem regressiva: ')).upper()
if n == 'SIM':
    for c in range(10,0,-1):
        sleep(1)
        print(c)
    print('*-*'*30)
    print('\033[1:35m FELIZ ANO NOVO \033[m')
    print('*-*'*30)
elif n != 'SIM':
    print('Ok, diga quando quiser que faremos ta?!')