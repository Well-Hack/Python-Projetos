print('Exercicio - 026 Faça um programa que leia uma frase pelo teclado e mostre \n Quantas vezes aparece a letra "A" '
       '\n Em que posição aparece pela primeira vez,  \n em que posição aparece a ultima vez')

nome = str(input('Por gentileza, digite o seu nome completo por favor: ')).strip()
nome2 = nome.upper().count('A')
print('Aparece {} vezes a letra "A"'.format(nome2))
nome3 = nome.upper().rfind('A')+1
print('A ultima vez que aparece a letrá A é {}'.format(nome3))
nome4 = nome.upper().split()
print('A primeira vez que aparece a Letra A é {} considerar 0 como inicio'.format(nome4[0].index('A')+1))
