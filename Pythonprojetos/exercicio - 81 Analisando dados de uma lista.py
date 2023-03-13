print('Exercicio - 81 Crie um programa que vai ler vários números e colocar em uma lista.\n '
      ' Depois disso, mostre:\n'
      ' A) Quantos números foram digitados. \n'
      ' B) A lista de valores, ordenada de forma decrescente. \n'
      ' C) Se o valor 5 foi digitado e está ou não na lista.')

print('=+'*30)
print('Analisando dados de uma lista')
print('=+'*30)

list = []
c = 0
while True:
    list.append(int(input('Digite um valor: ')))
    r = str(input('Deseja colocar mais um valor? [S/N]')).upper()
    c += 1
    if r == 'N':
        break
print(f'Você digitou {c} elementos.')
list.sort(reverse=True)
print(f'Você digitou os numeros em forma decrescente {list}')
if 5 in list:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')


