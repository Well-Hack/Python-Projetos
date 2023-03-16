print('Exercicio - 85 Crie um programa onde o usuário possa digitar sete valores numéricos e'
      ' cadastre-os em uma lista única que '
      'mantenha separados os valores pares e ímpares. No final, '
      'mostre os valores pares e ímpares em ordem crescente.')

print('=+'*30)
print('Lista composta e análise de dados')
print('=+'*30)

data = list()
par = list()
impar = list()
print('Olá, digite sete numeros separados que informaremos os pares e os impares')
for c in range(7):
        vlr = int(input(f'Digite o {c+1}º valor: '))
        data.append(vlr)
        if vlr % 2 == 0:
            par.append(vlr)
            print(f'Valor adicionado na lista de pares {par}')
        else:
            impar.append(vlr)
            print(f'Valor foi adicionado na lista de impares {impar}')
impar.sort()
par.sort()
print("=+"*50)
print(f'Os numeros foram: {data}')
print(f'Voce adicionou valores pares que foram: {par} ')
print(f'Vocẽ adicionou valores impares que são: {impar}')
print('Obrigado')

