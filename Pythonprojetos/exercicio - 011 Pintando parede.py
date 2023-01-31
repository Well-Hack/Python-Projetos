print('Exercicio 011 - Faça um programa que leia a largura e a altura de uma parede em metros. Calcule sua area \n'
      ' e a quantidade de tinta necessaria para pinta-la sabendo que cada litro de tinta pinta uma area de 2m²')
alt = float(input('Por gentileza, informe a ALTURA da párece: '))
lar = float(input('Por gentileza, informe a LARGURA da parece: '))
area = alt * lar / 2
print('Voce precisa de {} litros de tinta, para pintar uma altura de {} com largura de {}'.format(area,alt,lar))
