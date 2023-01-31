from calendar import datetime
print('Exercicio - 32 faça um programa que leia um ano qualquer e mostre se ele é bissexto')
ano = int(input('Digite o ano ou digite [1] para verificar o ano atual '))
if ano == 1:
    ano = datetime.datetime.now().year
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print('Ano Bissexto')
    else:
        print('Ano Comum')
else:
    if(ano%4==0 and ano % 100!= 0) or (ano%400==0):
        print('Ano Bissexto')
    else:
        print('Ano Comum')

