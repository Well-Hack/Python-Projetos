print('Desafio 13 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.')

print('=*' * 30)
print('Calculando Desconto')
print('=*' * 30)

sa = float(input('Por favor, digite o seu Salário: '))
sn1 = sa / 100 * 15
sn2 = sn1 + sa

print('Seu salario antigo é de {:.2f}, vai ter um aumento de 15% que vai ser de {:.2f}, e com isso, ficará no novo '
      '\n valor de {:.2f}'.format(sa, sn1, sn2))