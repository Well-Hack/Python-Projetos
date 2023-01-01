print('Desenvolva um programa que leia nome, idade e sexo de quatro pessoas e informe: \n'
      'A média de idade do grupo \n'
      'Qual é o nome do mais velho \n'
      'Quantas mulheres tem menos de 20 anos. ')
print('^^^'*30)
print('\033[1:32m ANALISADOR COMPLETO \033[m')
print('^^^'*30)
genero: [1,2]
idade = 0
idadem = 0
sexo = 0
for p in range (1,5):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(p)))
    idade2 = int(input('Digite a idade da {}ª pessoa '.format(p)))
    sexo2 = int(input('Digite 1 para masculino e 2 para feminino: '))
    idade += idade2
    media = idade / 4
    if idade2 > idadem:
        idadem = idade2
        velho = nome
    if idade2 < 20 and sexo2 == 2:
       sexo += 1
print('A média de idade do grupo é {:.0f}'.format(media))
print('O nome do mais velho seria {}'.format(velho))
print('E existem {} mulheres com menos de 20 anos'.format(sexo))