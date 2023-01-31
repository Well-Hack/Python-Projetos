print('Exercicio - 44 Elabore um programa que calcule o valor a ser pago por um produto. \n'
      'Considerando seu preço normal e condiçao de pagamento. \n'
      'A vista: 10% de desconto \n'
      'A vista no cartão: 5% de desconto \n'
      'Em até 2x no cartão: preço normal \n'
      'Acima de 3 vezes no cartão: 20% de juros')
print('+'*30)
print("Wellerson's Store")
print('+'*30)
p = float(input('Por favor, digite o valor do produto em R$: '))
m = int(input('Agora digite o metodo de pagamento conforme os digitos abaixo \n'
              '[1] Pagamento em Dinheiro \033[1:32m 10%  de desconto \033[m \n'
              '[2] Pagamento a vista no cartão de crédito \033[1:32m 5% de desconto \033[m \n'
              '[3] Pagamento em ATÉ 2x no cartão \033[1:33m preço normal \033[m \n'
              '[4] Pagamento acimde 3x ou mais no cartão \033[1:31m 20% de juros \033[m: '))
if m == 1:
    vlr = p - p * 0.10
    print('O valor do produto {} com desconto de 10% ficará no valor de \033[1:32m R${} \033[m'.format(p,vlr))
elif m == 2:
    vlr = p - p * 0.05
    print('O valor do produto {} com desconto de 5% ficará no valor de \033[1:32m R${} \033[m'.format(p, vlr))
elif m == 3:
    print('Você pagará o valor normal do produto que é \033[1:33m R${} \033[m'.format(p))
elif m == 4:
    pr = int(input('QUantas parcelas irá pagar: '))
    vlr = p + p/100*20
    pr2 = vlr / pr
    print('Você pagará pelo produto que era de R${}, passará com juros de 20% e ficará no valor de \033[1:31m R${} \033[m que \n'
          'será dividido em {}x e ficará no valor de cada parcela em \033[1:31m R${} \033[m'.format(p,vlr,pr,pr2))
else:
    print('\033[1:31m Digito Invalido \033[m')