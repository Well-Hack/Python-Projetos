print('Exercicio - 76 Crie um programa que tenha uma tupla única com nomes de produtos e \n'
      'seus respectivos preços, na sequência. No final, mostre uma listagem de preços, \n'
      ' organizando os dados em forma tabular. \n')

print('=+'*20)
print('Listagem de preços em Tuplas')
print('=+'*20)

list = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25, 'Apontador', 3.90, 'Mochila', 120.32, 'Caneta', 5.30)
for pos in range(0, len(list)):
    if pos % 2 == 0:
        print(f'{list[pos]:.<30}', end='')
    else:
        print(f'R$ {list[pos]:>.2f}')


