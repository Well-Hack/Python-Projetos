print('Exercicio - 78 Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. \n'
      'No final, mostre qual foi o maior e o menor valor digitado \n'
      'e as suas respectivas posições na lista.')

print('=+'*30)
print('Maior e menor valores em Listas')
print('=+'*30)

list = [int(input('Digite um valor: ')),
        int(input('Digite o Segundo valor: ')),
        int(input('Digite o Terceiro valor: ')),
        int(input('Digite o Quarto valor: ')),
        int(input('Digite o Quinto valor: '))]

print(f'Voce digitou {list}')
print(f'O menor numero digitado foi {min(list)}')
print(f'O maior numero digitado foi {max(list)}')
print('FIm do Programa')