nome = str(input('Olá! QUal é o seu nome? '))
n1 = float(input('Olá {}, por gentileza, digite a sua primeira nota: '.format(nome)))
n2 = float(input('Agora, digite a sua segunda nota! '))
m = (n1 + n2)/2
print('A sua média final foi: {:.1f}'.format(m))
if m >= 6:
    print('Você está aprovado {]! Parabéns!'.format(nome))
else:
    print('Você não atingiu a pontuação minima necessária para ser aprovado. Sinto Muito')