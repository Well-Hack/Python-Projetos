r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo Seguimento: '))
r3 = float(input('Terceiro Seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('O seguimentos acima podem formar um TRIANGULO')
else:
    print('Os seguimentos acima não formam um TRIANGULO')