print('+='*30)
print('Calculo de Investimento')
print('+='*30)

total = float(input('Digite o valor que voce vai querer investir para resgatar futuramente: '))
anof = int(input('Digite a daqui a quantos anos você ira querer resgatar esse valor: '))

anom = anof * 12
vlr = total / anom

print(f'Você tera que investir R${vlr:.2f} por mes, para que consiga resgatar o valor montante total daqui a {anof} anos ou {anom} meses')