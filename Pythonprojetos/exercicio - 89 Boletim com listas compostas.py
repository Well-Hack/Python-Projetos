print('Exercicio 89 - Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, \n'
      'mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.')

ficha = list()

while True:
    nome = str(input("Nome: "))
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    m1 = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], m1])
    resp = str(input("Você gostaria de continuar? (S = Sim, N = Não): ")).upper()
    if resp != 'S':
        break

print('=+' * 20)
print('Boletim dos Alunos:')
for aluno in ficha:
    print(f'Nome: {aluno[0]}')
    print(f'Notas: {aluno[1]}')
    print(f'Média: {aluno[2]}')
    print('=+' * 20)