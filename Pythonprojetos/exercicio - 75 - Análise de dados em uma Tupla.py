print('Exercicio - 75 esenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:'

'A) Quantas vezes apareceu o valor 9.'

'B) Em que posição foi digitado o primeiro valor 3.'

'C) Quais foram os números pares.')

print('=+'*30)
print('Análise de dados em uma Tupla')
print('=+'*30)

n1 = (int(input('Digite um numero: ')),
      int(input('Digite outro numero: ')),
      int(input('Digite mais um numero: ')),
      int(input('Digite o ultimo numero: ')))

print(f'Voce digitou os valores: {n1}')
print(f'O valor 9 apareceu {n1.count(9)} vezes')
print(f'O valor 3 apareceu na {n1.index(3)+1}ª posição')
print(f'Os valores pares, digitados foram',end='')

for n in n1:
    if n % 2 == 0:
        print(n, end=' ')