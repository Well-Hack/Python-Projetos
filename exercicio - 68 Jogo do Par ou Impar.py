print('Faça um programa que jogue \033[1:32m Par ou Impar \033[m com o computador O jogo só sera interrompido quando'
      '\n o jogador PERDER. Mostrando o total de vitórias consecutivas que ele conquistou no final do jogo ')
print('--'*30)
print('\033[1:34m PAR OU IMPAR\033[m')
print('--'*30)
print('Sera que voce consegue ganhar de mim? ;)')
from random import randint
cpu = 0
j1 = 0
v = 0
while True:
    j1 = int(input('Diga um valor: '))
    cpu = randint(0,10)
    total = j1 + cpu
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I} ')).strip().upper()[0]
    print(f'Voce jogou {j1} e o computador {cpu}. Total de {total}')
    if tipo =='P':
        if total % 2 == 0:
            print('VOCE VENCEU! ')
            v += 1
        else:
            print('VOCE PERDEU! ')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCE VENCEU! ')
            v += 1
        else:
            print('VOCE PERDEU! ')
            break
    print('Vamos jogar novamente... ')
print(f'GAME OVER, voce venceu {v} vezes.')







