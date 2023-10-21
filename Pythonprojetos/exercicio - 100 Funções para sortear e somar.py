print('Exercicio - 100 Faça um programa que tenha uma lista chamada números e \n'
      'duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear \n'
      '5 números e vai colocá-los dentro da lista e a \n'
      'segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.')
from time import sleep
from random import randint

def sorteia(lista):
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.3)
    print('PRONTO!')
def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

numeros = list()
sorteia(numeros)
somaPar(numeros)

