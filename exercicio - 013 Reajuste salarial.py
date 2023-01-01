print('Faça um programa que leia o salário de um funcionário e mostre esse novo salário com reajuste de 15%')
sal = float(input('Informe o valor do salario que aplicaremos o reajuste de 15%: '))
salr = sal / 100 * 15 + sal
print('O valor do salario que você recebia era R${}, e com reajuste de 15% fica R${:.2f}'.format(sal, salr))