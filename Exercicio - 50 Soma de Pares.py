print('Exercicio - 50  Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares \n'
      'Se o valor digitado for impar, desconsidere-o')
soma = 0
cont = 0
for n in range (1,7):
    n = int(input('Digite o {}º valor: '.format(n)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Voce me informou {} numeros pares e o total será {}'.format(cont,soma))

