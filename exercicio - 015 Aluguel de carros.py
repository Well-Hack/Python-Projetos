print('Exercicio 015 - Escreva um programa que pergunte a quantidade de kilometros percorrido pelo carro alugado e a quantidade'
      'de dias que ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60.00 por dia e R$0.15 por Km rodado ')
d = int(input('Quantos dias voce ficou com o carro: '))
km = float(input('Quantos Km foram rodados: '))
t = (60 * d)+ (0.15 * km)
print('O total a pagar é: R${:.2f}'.format(t))
