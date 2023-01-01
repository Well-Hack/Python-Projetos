print('Exercicio - 36 Desenvolvaum programa que leia o comprimento de tres retas e diga ao usuario se elas podem formar um triangulo')
r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo Seguimento: '))
r3 = float(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1+ r2:
    print('Os seguimentos acima podem formar um triangulo')
else:
    print('Os seguimentos acima não podem Formar o triangulo')