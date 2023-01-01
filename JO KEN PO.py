from random import randint
from time import sleep
print('-='*50)
print('JO KEN PO')
print('-='*50)
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
jogador = int(input('Escolha um numero de um a três \n [0] Papel \n [1] Pedra \n [2] Tesoura '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
sleep(0.5)
print('*'*21)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))

if computador == 0:
    if jogador == 0:
         print('JOGO EMPATOU')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
         print('Jogo invalido')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('JOGO EMPATOU')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('Jogo invalido')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('JOGO EMPATOU')
    else:
        print('Jogo invalido')
print('*'*21)
