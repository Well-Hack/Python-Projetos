print('Desafio 12 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.')

print('=*'*30)
print('Calculando Desconto')
print('=*'*30)

p1 = float(input('Por favor, digite o preço do produto: '))
d1 = p1 / 100 * 5
n1 = p1 - d1

print('O valor do seu produto é {:.2f}, com o desconto de 5% que seria de {:.2f}, vai ficar no novo valor de {:.2f}'.format(p1,d1,n1))
