print('Desafio 24 - Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.')

print('=*' * 30)
print('Verificando a primeira letra de um texto')
print('=*' * 30)

cid = str(input('Por favor digite o nome de sua cidade: ')).upper().split()


cid1 = 'SANTO' in cid

print(cid1)
