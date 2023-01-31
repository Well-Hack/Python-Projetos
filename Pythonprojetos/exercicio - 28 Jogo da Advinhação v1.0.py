import random
print('Exercicio - 028 Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 '
      '\n e peça ao usuario tentar descobrirqual foi o numero escolhido pelo computador. \n O programa deverá'
      'escrever na tela se o usuario venceu ou perdeu ')
print('-==-'*20)
print('Jogo da advinhação')
print('-==-'*20)
u1 = int(input('Digite um numero de 0 a 5 e tenta descobrir qual numero estou pensando: '))

n1 = random.randint(0,5)
if u1 == n1:
    print('Você ACERTOU, o numero na qual eu estava pensando era {} e voce escolheu {}'.format(n1,u1))
else:
    print('Você ERROU, o número na qual eu estava pensando era {} e você colocou {}'.format(n1,u1))