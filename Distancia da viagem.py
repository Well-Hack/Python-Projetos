nome = str(input('Olá! Qual é o seu nome? '))
Km = float(input('Tudo bem contigo {}? \nQual será a distancia de sua viagem em Km?'.format(nome)))
if Km <= 200.00:
    preco = float(0.50 * Km)
    print('O valor total que irá pagar em uma viagem onde a distancia é de {:.2f} é R${:.2f}'.format(Km,preco))
else:
    preco = float(0.45 * Km)
    print('O valor total que irá pagar em uma viagem onde a distancia é de {:.2f} é R${:.2f}'.format(Km,preco))