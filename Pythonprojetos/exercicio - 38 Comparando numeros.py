print('Exercicio - 038 Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem \n'
      'O primeiro valor é maior, O segundo valor é maior, Não existem valores maiores, os dois são iguais')
N1 = int(input('Digite o primeiro Numero: '))
N2 = int(input('Digite o segundo Numero: '))
if N1 > N2:
    print('O primeiro Numero é Maior')
elif N2 > N1:
    print('O segundo Numero é Maior ')
else:
    print('Os dois numeros são identicos')