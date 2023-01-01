from datetime import date
ano = int(input('Informe um determinado ano, e te informarei se ele é ou não bissexto, ou coloque 0 para analisar o ano atual '))
if  ano == 0:
    ano = date.today().year
if (ano%4==0 and ano%100!=0) or (ano%400==0):
         print('Bissexto')
else:
    print('Não é bissexto')