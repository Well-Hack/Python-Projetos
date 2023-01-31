print('Exercicio - 024 Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome SANTO')
nome = str(input('Por gentileza, informe o nome da cidade: ')).strip()
nome2 = (nome.upper())
nome3 = 'SANTO' in nome2[:6]
print(nome3)