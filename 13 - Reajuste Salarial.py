sal = float(input('Qual o valor do Salário atual do empregado? '))
aum = sal*0.15+sal
print('O empregado tinha um salário de R${:.2f}, com o aumento de 15% passa a ser o salário atual de R${:.2f}'.format(sal,aum))