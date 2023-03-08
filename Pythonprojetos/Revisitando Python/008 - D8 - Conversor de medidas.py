print('Desafio 8 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros. ')

print('=*'*30)
print('Conversor de medidas')
print('=*'*30)

n1 = int(input('Por favor, digite o valor em Metros: '))

mm1 = n1 * 1000
cm1 = n1 * 100

print(f'O valor que voce digitou em Metros foi {n1}, em centimentos fica {cm1} e em milimetros fica {mm1}')