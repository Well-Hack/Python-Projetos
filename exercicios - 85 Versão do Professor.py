print('Exercicio - 85 Crie um programa onde o usuário possa digitar sete valores numéricos e'
      ' cadastre-os em uma lista única que '
      'mantenha separados os valores pares e ímpares. No final, '
      'mostre os valores pares e ímpares em ordem crescente.')

print('=+'*30)
print('Lista composta e análise de dados')
print('=+'*30)


num = [[],[]]
valor = 0
for c in range(7):
    valor = int(input((f'Digite o {c+1}º valor: ')))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print('=='*30)
print(f'Todos os valores: {num}')
print(f'Os valores ṕares são {num[0]}')
print(f'Os valores impares são {num[1]}')


