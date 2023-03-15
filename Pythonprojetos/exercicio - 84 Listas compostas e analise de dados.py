print('Exercicio - 84 Faça um programa que leia nome e peso de várias pessoas,'
      'guardando tudo em uma lista. No final, mostre:  '
      'A) Quantas pessoas foram cadastradas.'
      'B) Uma listagem com as pessoas mais pesadas.'
      'C) Uma listagem com as pessoas mais leves.')

print('=+'*30)
print('Lista composta e análise de dados')
print('=+'*30)
cad = list()
data = list()
co = 0
lpes = list()
llev = list()
peso = 0
leve = 0

r = int(input('Vamos cadastrar? Sim[1] Não[2] '))
while True:
    if r == 1:
        data.append(str(input('Digite o seu nome: ')))
        data.append(int(input('Digite o seu peso: ')))
        if data[1] > 80:
            lpes.append(data[0])
            peso += 1
        else:
            llev.append(data[0])
            leve += 1
        cad.append(data[:])
        co += 1
        data.clear()
        r = int(input(('Deseja continuar? Sim[1] Não[2]: ')))
    else:
        break
print(f'Você cadastrou {co} pessoas \n'     
      f'Tem {peso} acima de 80 Kg que são {lpes}\n'
      f'Tem {leve} abaixo de 80 Kg que são {llev}')


