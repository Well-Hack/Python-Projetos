print('Exercicio - 25 Crie um programa que leia o nome de uma pessoa e veja se ela tem SILVA no nome')
nome = str(input('Por gentileza, digite o seu nome: ')).strip().upper()
nome2 = 'SILVA' in nome
print('seu nome tem silva? {}'.format(nome2))