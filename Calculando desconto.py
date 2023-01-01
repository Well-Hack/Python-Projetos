nome = str(input('Por gentileza, informe o seu nome: '))
prod = float(input('Qual o valor total do produto em R$ '))
pag = int(input('''Qual será a forma de pagamento:
 [1] pagamento à vista no Dinheiro
 [2] pagamento à vista no Cartão de Cŕedito
 [3] pagamento parcelado em até 2x no cartão 
 [4] pagamento para as demais parcelas: 
 '''))
if pag == 1:
    final = prod - (prod * 0.10)
    print('Você irá pagar um valor total com desconto de \33[1;34m 10% \33[m o valor de R$ {:.2f}'.format(final))
elif pag == 2:
    final = prod - (prod * 0.05)
    print('Você pagará um valor total com desconto de \33[1;34m 5% \33[m o valor de R$ {:.2f}'.format(final))
elif pag == 3:
    final = prod / 2
    print('Você pagará o valor total de R$ {:.2f} dividido em duas vezes no valor de R$ {:.2f}'.format(prod, final))
elif pag == 4:
    parc = int(input('''Digite a quantidade de vezes que você vái dividir acima de 2 parcelas:
     [1] para dividir em 3 vezes
     [2] para dividir em 4 vezes 
     [3] para dividir em 5 vezes
     [4] para dividir em 6 vezes
     '''))
    if parc == 1:
       final = prod + (prod * 0.20)
       parce = final / 3
       print('Você pagará o valor de R$ {:.2f} com acréscimo de juros de 20% no valor total de R${:.2f} dividido em 3 '
             'vezes no valor de R${}'.format(prod, final, parce))
    elif parc == 2:
       final = prod + (prod * 0.20)
       parce = final / 4
       print('Você pagará o valor de R$ {:.2f} com acréscimo de juros de 20% no valor total de R${:.2f} dividido em 4 '
             'vezes no valor de R${}'.format(prod, final, parce))
    elif parc == 3:
       final = prod + (prod * 0.20)
       parce = final / 5
       print('Você pagará o valor de R$ {:.2f} com acréscimo de juros de 20% no valor total de R${:.2f} dividido em 5 '
             'vezes no valor de R${}'.format(prod, final, parce))
    elif parc == 4:
       final = prod + (prod * 0.20)
       parce = final / 6
       print('Você pagará o valor de R$ {:.2f} com acréscimo de juros de 20% no valor total de R${:.2f} dividido em 6 '
             'vezes no valor de R${}'.format(prod, final, parce))
    elif parc == 5 or 6 or 7 or 8 or 9:
        print('Opção errada, tente novamente')
elif pag == 5 or 6 or 7 or 8 or 9:
    print('Opção errada, tente novamente')
