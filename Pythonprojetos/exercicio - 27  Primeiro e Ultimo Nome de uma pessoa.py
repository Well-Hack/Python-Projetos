print('exercicio - 027 Faça um programa que leia o nome completo de uma pessoa, \n mostrando em seguida o primeiro e o ultimo nome dessa pessoa')
nome = str(input('Por gentileza, digite seu nome completo: '))
nome2 = nome.split()
nome3 = nome2[-1]
print('O seu primeiro nome é {}, e o seu ultimo nome seria {}'.format(nome2[0],nome3))