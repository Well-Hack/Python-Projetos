import random
print('Olá! Bem vindo ao jogo da adivinhação! @-@')
nome = str(input('Por gentileza, diga-me o teu nome: '))
print('Certo {}, eu vou pensar em um número, e você tenta adivinhar qual número eu pensei.'.format(nome))
n1 = int(input('Fale um número de 0 a 6! '))
vl = (random.randrange(0, 6))
if n1 == vl:
    print('Parabéns você acertou o número que eu pensei! Seu número:{} Meu número:{}'.format(n1,vl))
else:
    print('Infelizmente você errou! Quem sabe a próxima? Seu número:{} Meu número:{}'.format(n1,vl))