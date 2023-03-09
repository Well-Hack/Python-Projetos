print('Desafio 14 - AEscreva um programa que pergunte a quantidade de Km percorridos por um carro alugado'
      ' e a quantidade de dias \n pelos quais ' 
      'ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.')

print('=*' * 30)
print('Aluguel de Carros')
print('=*' * 30)

d = int(input('Quantos dias voce ficará com o automóvel: '))
km = float(input('Quantos Km foram rodados: '))
t = (60 * d) + (0.15 * km)
print('O total a pagar é: R${:.2f}'.format(t))