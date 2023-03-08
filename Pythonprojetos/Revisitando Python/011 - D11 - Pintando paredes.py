print('Desafio 11 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade '
      '\n de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados. ')

print('=*'*30)
print('Pintando paredes')
print('=*'*30)

l1 = float(input('Por favor, digite a largura da parede que voce vai pintar: '))
a1 = float(input('Agora digite a altura da parede em que você vai pintar: '))

area = l1 * a1
t1 = area / 2

print('Sua parede tem como dimensão {:.2f} x {:.2f} o que da uma area de {} \n'
      'com isso você precisara de {}l de tinta' .format(l1,a1,area,t1))