print('Exercicio 012 - Faça um algoritmo que leia o preço de um produto e mostre o preço novo com 5% de desconto')
pr = float(input('Informe o valor do produto que aplicaremos o desconto de 5%: '))
prn = pr - (pr * 5 / 100)
print('O valor do produto que você colocou foi R${}, e com desconto de 5% fica R${:.2f}'.format(pr, prn))