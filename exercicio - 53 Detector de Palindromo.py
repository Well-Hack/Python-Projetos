print('Exercicio - 53 Crie um programa que leia uma frase qualquer e diga se ele éum PALINDROMO')
R = str(input('Diga qualquer frase que iremos informar se ele é um Palindromo: ')).upper().replace(' ','')
R2 = R[::-1]
print(R2)
if R[0:] == R2 :
    print('É um palindromo')
else:
    print('Não é Palindromo')