import random
print('Exercicio - 58 Melhore o jogo do desafio 28 onde o computador vai "pensar" em um numero de 0 a 10. \n'
      'Só que agora o jogador vai tentar adivinhar até acertar. Mostrando no final quantos palpites foram \n'
      'necessarios para vencer')
print('-==-'*20)
print('\033[032:1m JOGO DA ADIVINHAÇÃO \033[m')
print('-==-'*20)
s = 0
j1 = int(input('Tente adivinhar qual numero estou pensando de 0 a 10: '))
cpu = random.randint(0,10)
while j1 != cpu:
    s += 1
    print('Errou, não foi dessa vez')
    j1 = int(input('Tente novamente: '))
print('Acertou')
print('Você tentou {} vezes, voce digitou {} e a maquina digitou {}'.format(s,j1,cpu))


