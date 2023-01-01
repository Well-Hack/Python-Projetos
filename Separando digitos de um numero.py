n1 = int(input('Digite um núemro: '))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
print('Analisando o número{}'.format(n1))
print('Contem o numero {} como unidade'.format(u))
print('Contem o numero {} como dezena'.format(d))
print('Contem o numero {} como centena'.format(c))
print('Contem o numero {} como milhar'.format(m))