print('Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos. ')

pmaior = 0
pmenor = 0
for p in range(1,6):
    peso = float(input('Informe o seu peso em Kg: '))
    if p == 1:
        pmaior = peso
        pmenor = peso
    else:
        if peso > pmaior:
            pmaior = peso
        if peso < pmenor:
            pmenor = peso
print('O maior peso lido foi {}Kg'.format(pmaior))
print('O menor  peso lido foi {}Kg'.format(pmenor))
