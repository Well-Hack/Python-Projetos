print('Exercicio - 42 Refaça o DESAFIO 35 dos triângulos,  \n'
      'acrescentando o recurso de mostrar que tipo de triângulo será formado.')
r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo Seguimento: '))
r3 = float(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1+ r2:
    print('Os seguimentos acima podem formar um triangulo! ', end='')
    if r1 == r2 and r2 == r3:
        print('EQUILATERO')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('ESCALENO')
    elif r1 != r2 and r2 != r3 and r1 == r3 or r2 == r3:
        print('ISÓSCELES')
else:
    print('Os seguimentos acima não podem Formar o triangulo')