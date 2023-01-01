vel = (float(input('Qual a velocidade atual do seu carro? ')))
if vel > 80:
    multa = float((vel - 80 ) * 7)
    print('Você ultrapassou o limite de velocidade de 80Km/h.')
    print('Pagará uma multa no valor de R${:.2f}.'.format(multa))
else:
    print('Velocidade permitida, dirija com segurança')