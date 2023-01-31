print('Faça um exercicio que leia um numero que leia um numero qualquer e mostre seu fatorial. ')
print('&'*70)
print('\033[032:1m CALCULO FATORIAL \033[m')
print('&'*70)
n1 = 1
n1 = int(input('Por gentileza, digite um numero qualquer: '))
total = n1
while n1 != 1:
    n1 -= 1
    total = total * n1
print('O resultado é {}'.format(total))



