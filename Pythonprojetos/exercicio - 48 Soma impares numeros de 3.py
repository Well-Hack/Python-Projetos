print('Exercicio - 48 Faça um programa que calcule a soma entre todos os numeros impares que são multiplos de 3 \n'
      'e que se encontram no intervalo de 1 a 500')
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('A soma de todos os {} valores solicitados é {}.'.format(cont,soma), end=' ')