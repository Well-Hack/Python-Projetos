print('Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:\n'
      ' início, fim e passo. Seu programa tem que realizar três contagens através da função criada:')
from time import sleep
def contador(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
    print('-'*20)
    print(f'Contagem de {i} até o {f} de {p} em {p}')
        while cont <= f:
            print(f'{cont}', end='', flush=True)
            sleep(0.8)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end='', flush=True)
            sleep(0.8)
            cont -= p
        print('FIM!')
    print('-' * 20)


contador(0,10, 1)
contador(10,0, 2)
print('Agora é a sua vez de personalizar a contagem! ')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)