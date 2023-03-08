print('Desafio 10 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira R$ e mostre quantos dólares ela pode comprar. ')

print('=*'*30)
print('Conversor em Dólares')
print('=*'*30)


r1 = float(input('Por gentileza, digite o valor em Reais(BRL), do quanto voce quer converter para dólares: '))
d1 = r1 / 5.14

print('Voce pode comprar {:.2f} em Dólares (USD) com esse valor em {:.2f} Reais (BRL)'.format(d1,r1))