Prod = float(input('Qual o valor do produto: '))
Desc = float(input('Qual o valor do desconto que será aplicado:'))
PF =  Prod-(Prod*Desc)/100
print('O valor do produto  R${:.2f} com aplicação de {:.2f}% de desconto, o preço final ficará em R${:.2f}'.format(Prod,Desc,PF))