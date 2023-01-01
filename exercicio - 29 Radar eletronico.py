print('exercicio - 29 Escreva um programa que leia a velocidade de um carro se ele ultrapassar 80 Km/h ,  mostre uma mensagem \n'
      'a multa vai custar R$7,00 a cada Km/h acima do limite')
vel = float(input('Qual velocidade o carro estava: '))
if vel > 80:
    vel2 = (vel - 80) * 7
    print('Voce estava á {:.1f}Km acima da velocidade permitida, vai pagar uma multa de R${:.2f}'.format(vel,vel2))
else:
    print('Não há multa')