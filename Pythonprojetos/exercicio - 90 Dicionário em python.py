print('Exercicio 90 - Faça um programa que leia nome e média de um aluno, \n'
      'guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.')

print('*='*30)
print('ANALISADOR DE MÉDIA')
print('*='*30)

aluno = dict()
aluno2 = list()

aluno['aluno'] = str(input('Digite o nome do aluno: '))
aluno['nota'] = int(input('Qual foi a nota do aluno?: '))
aluno2 = aluno.copy()
if aluno['nota'] <= 6:
    aluno['média'] = 'Reprovado'
    aluno2 = aluno.copy()
else:
    aluno['média'] = 'Aprovado'
    aluno2 = aluno.copy()
print(f'O nome do aluno seria: {aluno2["aluno"]}, a nota dele foi: {aluno2["nota"]} e ele foi: {aluno2["média"]} ')

