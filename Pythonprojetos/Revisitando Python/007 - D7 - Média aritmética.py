print('Desafio 7 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média. ')

print('=*'*30)
print('Média aritmética')
print('=*'*30)

print('Analise de Aprovação de aluno! ')
n1 = int(input('Por gentileza! Digite a primeira nota do Aluno: '))
n2 = int(input('Agora digite a segunda Nota do Aluno: '))
n3 = int(input('Digite a ultima nota do aluno: '))

m1 = (n1 + n2 + n3) / 3

if m1 <= 6:
  print(f'O aluno não foi \033[035:1m REPROVADO! \033[m A primeira nota foi {n1}, a segunda {n2} e a terceira {n3}, o resultado final deu {m1}')
else:
    print(f'O aluno foi \033[032:1m APROVADO \033[m. O resultado final deu {m1}')