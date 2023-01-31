print('Exercicio - 64 Crie um programa que leia varios numeros inteiros pelo teclado. O programa'
      ' so vai parar quando o usuario digitar 999. que é a condição de parada., No final, mostre quantos'
      'numeros foram digitados e qual foi a soma entre eles')
soma = 0
n1 = 0
soma2= 0
while n1 != 999:
    n1 = int(input('Digite um numero Qualquer de 0 a 998, o 999 voce saira do programa: '))
    soma2 = n1 + soma2
    if n1 != 999:
        soma += 1
print('Você digitou {} numeros e o resultado final foi {}'.format(soma,soma2 - 999))