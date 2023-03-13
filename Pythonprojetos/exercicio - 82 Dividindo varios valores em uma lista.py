print('Exercicio - 82  Crie um programa que vai ler vários números e colocar em uma lista. \n'
      ' Depois disso, crie duas listas extras que vão conter \n'
      ' apenas os valores pares e os valores ímpares digitados, \n'
      ' respectivamente. Ao final, mostre o conteúdo das três listas geradas.')

print('=+'*30)
print('Dividindo valores em várias listas')
print('=+'*30)

num = []
par = []
impar = []
while True:
    num.append(int(input('Digite um valor: ')))
    r = str(input('Deseja colocar mais um valor? [S/N]')).upper()
    if r == 'N':
        break
for i,v in enumerate(num):
    if v % 2 == 0:
       par.append(v)
    else:
        impar.append(v)
print(f'Os numeros que voce digitou foram:{num}')
print(f'Os numeros pares que voce digitou foram:{par}')
print(f'Os numeros impares que voce digitou foram:{impar}')