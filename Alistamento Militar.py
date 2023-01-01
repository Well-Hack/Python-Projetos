from datetime import date
ano = int(input('Por gentileza, digite o ano que voce nasceu '))
year = date.today().year
res = year - ano
falta = 18 - res
passou = res - 18
print('Você tem {} anos'.format(res))
if res < 18:
    print('Ainda falta {} anos para você se alistar'.format(falta))
    print('Você ainda não está no ano de Alistamento')
if res == 18:
    print('Você está no ano de alistamento, por gentileza, procurar uma junta militar para se alistar')
else:
    print('ATENÇÃO, você já passou do ano de seu alistamento, caso ainda não tenha comparecido a uma junta militar.\n por favor,'
          'realize a procurar de uma mais próxima. Você está a {} anos atrasado'.format(passou))