print("Exercicio 88 - Palpite mega-sena. \n"
      "Faça um programa que ajude um jogador da MEGA SENA a criar palpites.\n"
      "O programa vai perguntar quantos jogos serão gerados \n"
      "e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta")
from random import randint
from time import sleep
lista = list()
jogos = list()
print('=+'*50)
print('Sorteio da mega sena')
print('=+'*50)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('=+'*50)
print('SORTEANDO JOGOS')
for i, l in enumerate(jogos):
    print(f'jogos {i+1}: {l}')
    sleep(2.5)
print('=+' * 50)
