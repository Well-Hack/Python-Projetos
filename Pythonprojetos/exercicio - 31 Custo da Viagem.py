print ('Exercicio - 31 Desenvolva um programa que pergunte a distancia de uma viagem em Km. Calcule o preço da passagem, '
       'cobrando R$0,50 por Km rodado para viagens até 200Km e R$0,45 para viagens mais longas')
vi = float(input('Digite a distancia da viagem em Km: '))
if vi <= 200:
    vlr= vi * 0.50
    print('O valor da sua viagem custará R$ {:.2f} devido a distancia de Km {:.2f}'.format(vlr,vi))
else:
    vlr = vi * 0.45
    print('O valor da sua viagem custará R${:.2f} devido a distancia de Km {:.2f}'.format(vlr,vi))
