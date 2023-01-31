print('Exercicio - 40 Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no \n'
      'final de acordo com sua média atingida. Acima de 6 APROVADO, entre 4 e 5 RECUPERAÇÃO e abaixo de 4 REPROVADO')
print('='*80)
print('ANALISADOR DE NOTAS')
print('='*80)
nome = str(input('Por gentileza, digite o \033[1:32m nome \033[m do aluno: '))
n1 = float(input('Digite a primeira nota do {}: '.format(nome)))
n2 = float(input('Digite a segunda nota do {}: '.format(nome)))
m = (n1 + n2) / 2
if m > 7:
    print('O aluno {} está \033[1:32m APROVADO \033[m com a média {:.2f}'.format(nome,m))
elif m > 5 and m < 6.9:
    print('O aluno {} está de \033[1:33m RECUPERAÇÃO \033[m com a média {:.2f}'.format(nome,m))
else:
    print('O aluno {} está de \033[1:31m REPROVADO \033[m com a média {:.2f}'.format(nome,m))
