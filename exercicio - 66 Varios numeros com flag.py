print('Exercicio - 64 Crie um programa que leia varios numeros inteiros pelo teclado. O programa'
      ' so vai parar quando o usuario digitar 999. que é a condição de parada., No final, mostre quantos'
      'numeros foram digitados e qual foi a soma entre eles')
n1 = soma = soma2 = 0
while True:
    n1 = int(input('Digite um numero Qualquer de 0 a 998, o 999 voce saira do programa: '))
    if n1 == 999:
        break
    soma2 += n1
    soma += 1
print(f'Você digitou {soma} valores que totalizou {soma2}')