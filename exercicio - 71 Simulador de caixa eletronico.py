print('Exercicio - 71Crie um programa que simule um caixa eletronico. No inicio, pergunte ao usuario \n'
      'qual valor sera sacado (numeros inteiros) e o programa vai informar quantas cédulas de cada \n valor serão'
      ' entregues valores das cedulas: 1,10,20,50')
print('='*30)
print('BANCO CURSO EM VIDEO')
print('='*30)
valor = int(input('Qual valor de saque R$: '))
total = valor
ced = 50
totced = 0
while True:
      if total >= ced:
            total -= ced
            totced += 1
      else:
            if totced > 0:
                  print(f'Total de {totced} cedulas de {ced}')
            if ced == 50:
                  ced = 20
            elif ced == 20:
                  ced = 10
            elif ced == 10:
                  ced = 1
            totced = 0
            if total == 0:
                  break