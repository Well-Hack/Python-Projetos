print('Exercicio - 45 Jo Ken Po')
from random import randint
from time import sleep
itens = ('pedra','papel','tesoura')
cpu = randint(0,2)
print('''Suas opções:
         [0] Pedra
         [1] Papel
         [2] Tesoura''')
jogador = int(input('Qual é a sua jogada: '))
print('=-'*20)
print('Maquina jogou {}'.format(itens[cpu]))
print('Jogador jogou {}'.format(itens[jogador]))
print('=-'*20)

if cpu == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador VENCEU')
    elif jogador == 2:
        print('Jogador PERDEU')
    else:
        print('Jogada invalida')
elif cpu == 1:
    if jogador == 0:
        print('Jogador PERDEU')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador VENCEU')
    else:
        print('Jogada invalida')
elif cpu == 2:
    if jogador == 0:
        print('Jogador VENCEU')
    elif jogador == 1:
        print('Jogador PERDEU')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada invalida')