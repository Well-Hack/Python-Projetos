v1 = int(input('Digite o 1º valor: '))
v2 = int(input('Digite o 2º valor: '))
v3 = int(input('Digite o 3º valor: '))
if v1<v2 and v1<v3:
    menor = v1
if v2<v1 and v2<v3:
    menor = v2
if v3<v1 and v3<v2:
    menor = v1
if v1>v2 and v1>v3:
    maior = v1
if v2 > v1 and v2>v3:
    maior = v2
if v3 > v1 and v3>v2:
    maior = v3
print('O maior valor é {} \n O menor valor é {}.'.format(maior,menor))