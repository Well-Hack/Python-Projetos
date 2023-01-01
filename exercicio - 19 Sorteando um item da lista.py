import random
print('Exercicio 19 - Um professor quer sortear um dos quatro alunos para apagar um quadro.'
      'faça um programa que ajude a ele escolher lendo o nome deles e escrevendo o nome do escolhido ')
a1 = str(input('Qual o nome do primeiro aluno? '))
a2 = str(input('Qual o nome do segundo aluno? '))
a3 = str(input('Qual o nome do terceiro aluno? '))
a4 = str(input('Qual o nome do quarto aluno? '))

print('A pessoa que vai apagar o quadro vai ser o {}'.format(random.choice([a1,a2,a3,a4])))
